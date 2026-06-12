import pytest
from playwright.sync_api import Page, expect
from pages.support_page import TicketListPage, NewTicketPage


def test_ticket_list_shows_default_tickets(page: Page):
    """La liste affiche les 2 tickets par défaut."""
    p = TicketListPage(page)
    p.navigate()
    titles = p.get_ticket_titles()
    assert len(titles) == 2
    assert "Login ne fonctionne pas" in titles


def test_open_count_is_correct(page: Page):
    """Le compteur de tickets ouverts affiche 2 au départ."""
    p = TicketListPage(page)
    p.navigate()
    assert p.get_open_count() == 2


def test_new_ticket_link_navigates(page: Page):
    """Cliquer sur 'Nouveau ticket' amène sur le formulaire."""
    p = TicketListPage(page)
    p.navigate()
    p.go_to_new_ticket()
    expect(page).to_have_url("http://localhost:5001/tickets/new")


def test_submit_valid_ticket_appears_in_list(page: Page):
    """Soumettre un ticket valide l'ajoute à la liste."""
    form = NewTicketPage(page)
    form.navigate()
    form.fill_title("Impossible de se connecter")
    form.select_category("Bug")
    form.fill_description("Le bouton login ne répond pas.")
    form.submit()

    expect(page).to_have_url("http://localhost:5001/tickets")
    p = TicketListPage(page)
    assert "Impossible de se connecter" in p.get_ticket_titles()


def test_submit_empty_title_shows_error(page: Page):
    """Soumettre sans titre affiche une erreur inline."""
    form = NewTicketPage(page)
    form.navigate()
    form.select_category("Question")
    form.submit()

    expect(page).to_have_url("http://localhost:5001/tickets/new")
    assert form.get_title_error() == "Le titre est requis."


def test_resolve_ticket_changes_status(page: Page):
    """Cliquer sur 'Résolu' change le statut du ticket."""
    p = TicketListPage(page)
    p.navigate()
    p.resolve_ticket(1)

    expect(page).to_have_url("http://localhost:5001/tickets")
    assert p.get_ticket_status(1) == "Résolu"


def test_cancel_button_redirects_to_ticket_list(page: Page):
    """Cliquer sur annuler redirige vers la page principale"""
    p = TicketListPage(page)
    p.navigate()
    p.go_to_new_ticket()
    expect(page).to_have_url(NewTicketPage.URL)
    form = NewTicketPage(page)
    form.submit_cancel()
    expect(page).to_have_url(TicketListPage.URL)


def test_resolve_ticket_decrements_open_count(page):
    p = TicketListPage(page)
    p.navigate()
    p.resolve_ticket(1)
    assert p.get_open_count() == 1
