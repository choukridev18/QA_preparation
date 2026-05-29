from sys import exec_prefix
import pytest
from playwright.sync_api import Page, expect
from pages.booking_page import BookingPage


def test_complete_booking_flow(page: Page, app_url: str):
    """Remplir les 3 étapes et confirmer → page de succès"""
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("Marie Martin", "marie@example.com")
    booking.submit_step1()
    booking.fill_step2("20/06/2026", 2)
    booking.submit_step2()
    booking.confirm()
    expect(page).to_have_url(f"{app_url}/done")
    assert "Marie Martin" in booking.get_success_message()


def test_missing_name_shows_error(page: Page, app_url: str):
    """Soumettre l'étape 1 sans nom → message d'erreur visible"""
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("", "test@example.com")
    booking.submit_step1()
    expect(page).to_have_url(f"{app_url}/step1")
    assert booking.get_error_message() != ""


def test_summary_shows_entered_data(page: Page, app_url: str):
    """Le récapitulatif affiche bien les données saisies"""
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("Paul Durand", "paul@example.com")
    booking.submit_step1()
    booking.fill_step2("10/08/2026", 4)
    booking.submit_step2()
    assert booking.get_summary_name() == "Paul Durand"


def test_invalid_email_shows_error(page: Page, app_url: str):
    """l'adresse email est incomplete"""
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("choukri", "choukri18")
    booking.submit_step1()
    assert booking.get_error_message() != ""


def test_invalide_date_shows_error(page: Page, app_url: str):
    """la date n'a pas été remplie"""
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("Paul Durand", "paul@example.com")
    booking.submit_step1()
    booking.fill_step2("", "5")
    booking.submit_step2()
    assert booking.get_error_message() != ""


def test_try_step2_without_fill_step1(page: Page, app_url: str):
    """essayer de passer a step2 sans remplir step1"""
    booking = BookingPage(page)
    booking.navigate()
    page.goto(f"{app_url}/step2")
    expect(page).to_have_url(f"{app_url}/step1")


def test_check_date_step3(page: Page, app_url: str):
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("Paul Durand", "paul@example.com")
    booking.submit_step1()
    booking.fill_step2("10/08/2026", "5")
    booking.submit_step2()
    date = booking.page.locator("#summary-date").inner_text()
    assert date == "10/08/2026"


def test_check_numbers_personnes(page: Page, app_url: str):
    booking = BookingPage(page)
    booking.navigate()
    booking.fill_step1("Paul Durand", "paul@example.com")
    booking.submit_step1()
    booking.fill_step2("10/08/2026", "5")
    booking.submit_step2()
    assert booking.get_summary_guests() == "5"


def test_page_done_redirection_step1(page: Page, app_url: str):
    booking = BookingPage(page)
    booking.navigate()
    booking.page.goto(f"{app_url}/done")
    expect(page).to_have_url(f"{app_url}/step1")
