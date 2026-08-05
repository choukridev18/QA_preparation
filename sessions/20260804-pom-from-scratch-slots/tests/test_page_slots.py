from playwright.sync_api import Page, expect
from pages.slots_page import SlotsPage, ConfirmationPage


def test_book_valide_slot(page: Page):
    """Reservé un creneau valide"""
    s = SlotsPage(page)
    s.navigate()
    s.choice_one_slot("Lundi 9h00")
    s.submit_slot()
    expect(page).to_have_url(f"{ConfirmationPage.URL}slot-1")


def test_get_error_message_if_slot_already_booked(page: Page):
    """Reservé un creneau deja reservé affiche un message d'erreur"""
    s = SlotsPage(page)
    s.navigate()
    s.choice_one_slot("Lundi 9h00")
    s.submit_slot()
    c = ConfirmationPage(page)
    c.return_main_page()
    s.choice_one_slot("Lundi 11h00")
    s.submit_slot()
    assert s.get_error_message() == "Vous avez déjà une réservation en cours."


def test_cancel_reservation_redirect_main_list(page: Page):
    """annuler une reservation renvoi à la liste  principal"""
    s = SlotsPage(page)
    s.navigate()
    s.choice_one_slot("Lundi 9h00")
    s.submit_slot()
    c = ConfirmationPage(page)
    c.return_main_page()
    s.cancel_booking()
    expect(page).to_have_url(SlotsPage.URL)


def test_get_error_message_if_book_without_selection_slot(page: Page):
    """ " reserver sans selectionner de creneau affiche un message d'erreur"""
    s = SlotsPage(page)
    s.navigate()
    s.submit_slot()
    assert s.get_error_message() == "Veuillez sélectionner un créneau."
