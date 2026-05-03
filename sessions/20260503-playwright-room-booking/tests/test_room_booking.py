"""Tests fournis — à faire passer en implémentant les Page Objects."""

from datetime import date, timedelta

from playwright.sync_api import Page, expect

from pages.booking_step1_page import BookingStep1Page
from pages.booking_step2_page import BookingStep2Page
from pages.booking_step3_page import BookingStep3Page
from pages.booking_success_page import BookingSuccessPage


def _future_date_iso(days_ahead: int = 14) -> str:
    return (date.today() + timedelta(days=days_ahead)).isoformat()


def test_complete_booking_flow_shows_reference(page: Page):
    """Parcours complet : étapes 1→2→3 puis page succès avec une référence BK-."""
    iso = _future_date_iso()
    step1 = BookingStep1Page(page)
    step1.navigate()
    step1.fill_booking_date(iso)
    step1.select_room("Grande salle")
    step1.click_next()

    expect(page).to_have_url("http://localhost:5001/booking/step2")

    step2 = BookingStep2Page(page)
    step2.select_time_slot("Après-midi (14h–17h)")
    step2.set_attendees(6)
    step2.click_next()

    expect(page).to_have_url("http://localhost:5001/booking/step3")

    step3 = BookingStep3Page(page)
    assert step3.get_recap_date_text().strip() == iso
    assert step3.get_recap_room_text().strip() == "Grande salle"
    step3.confirm_booking()

    expect(page).to_have_url("http://localhost:5001/booking/success")

    success = BookingSuccessPage(page)
    ref = success.get_booking_reference().strip()
    assert ref.startswith("BK-")


def test_step2_without_prior_booking_redirects_to_step1(page: Page):
    """Sans session, accéder à l'étape 2 doit renvoyer vers l'étape 1."""
    step2 = BookingStep2Page(page)
    step2.navigate()

    expect(page).to_have_url("http://localhost:5001/booking/step1")


def test_step3_without_prior_booking_redirects_to_step1(page: Page):
    """Sans session, accéder à l'étape 3 doit renvoyer vers l'étape 1."""
    step3 = BookingStep3Page(page)
    step3.navigate()

    expect(page).to_have_url("http://localhost:5001/booking/step1")

def test_success_page_without_booking_redirects_to_step1(page: Page):
    """Sans réservation en session, /booking/success renvoie vers l'étape 1."""
    page.goto("http://localhost:5001/booking/success")
    expect(page).to_have_url("http://localhost:5001/booking/step1")



def test_complete_booking_flow_alternate_choices(page: Page):
    """Parcours complet : étapes 1→2→3 puis page succès avec une référence BK-."""
    iso = _future_date_iso()
    step1 = BookingStep1Page(page)
    step1.navigate()
    step1.fill_booking_date(iso)
    step1.select_room("Petite salle")
    step1.click_next()

    expect(page).to_have_url("http://localhost:5001/booking/step2")

    step2 = BookingStep2Page(page)
    step2.select_time_slot("Matin (9h–12h)")
    step2.set_attendees(6)
    step2.click_next()

    expect(page).to_have_url("http://localhost:5001/booking/step3")

    step3 = BookingStep3Page(page)
    assert step3.get_recap_date_text().strip() == iso
    assert step3.get_recap_room_text().strip() == "Petite salle"
    step3.confirm_booking()

    expect(page).to_have_url("http://localhost:5001/booking/success")

    success = BookingSuccessPage(page)
    ref = success.get_booking_reference().strip()
    assert ref.startswith("BK-")
