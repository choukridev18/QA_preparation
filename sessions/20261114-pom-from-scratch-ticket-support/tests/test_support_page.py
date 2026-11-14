from pages.support_page import SupportPage
from playwright.sync_api import expect


def test_create_ticket(page):
    create = SupportPage(page)
    create.navigate()
    create.fill_field_subject("Identifiant")
    create.choice_priority("Haute")
    create.write_in_field_message("le bouton ne fait rien")
    create.submit()
    assert create.get_message_success_creation() == "Ticket créé avec succès."
    assert "Identifiant" in create.get_visibility_tickets()


def test_support_from_is_visible(page):
    visible = SupportPage(page)
    visible.navigate()
    expect(visible.page.get_by_label("Sujet")).to_be_visible()
    expect(visible.page.get_by_label("Priorité")).to_be_visible()
    expect(visible.page.get_by_label("Description")).to_be_visible()
    expect(visible.page.get_by_role("button", name="Créer le ticket")).to_be_visible()


def test_get_list_empty_ticket(page):
    message = SupportPage(page)
    message.navigate()
    assert message.get_empty_message_ticket() == "Aucun ticket pour le moment."
