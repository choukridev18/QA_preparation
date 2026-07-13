import pytest
from playwright.sync_api import Page
from pages.contacts_page import Contacts


def test_add_contact_valide(page: Page):
    """Ajouter un contact valide"""
    c = Contacts(page)
    c.navigate()
    c.add_contact("Chokri Bourassi", "choukridev18@gmail.com", "0612908518")
    assert "Chokri Bourassi" in page.locator(".contact-name").all_inner_texts()


def test_add_email_already_used(page):
    """Ajouter un email deja utilisé affiche un message d'erreur"""
    c = Contacts(page)
    c.navigate()
    c.add_contact("Chokri Bourassi", "choukridev18@gmail.com", "0612908518")
    assert "Chokri Bourassi" in page.locator(".contact-name").all_inner_texts()
    c.add_contact("Chokri", "choukridev18@gmail.com", "0000000000")
    assert "Cet email est déjà utilisé." in c.get_error_message()


def test_add_contact_with_field_name_empty(page):
    """Ajouter un contact en laissant le champs nom vide affiche un message d'erreur"""
    c = Contacts(page)
    c.navigate()
    c.add_contact("", "choukridev18@gmail.com", "0612908518")
    assert "Le nom est obligatoire." in c.get_error_message()


def test_get_list_name_with_search(page):
    """Appuyer sur le bouton 'rechercher' affiche les contacts correspondants"""
    c = Contacts(page)
    c.navigate()
    c.add_contact("Chokri Bourassi", "choukridev18@gmail.com", "0612908518")
    c.search_contacts("Chokri")
    assert "Chokri Bourassi" in c.page.locator(".contact-name").all_inner_texts()


def test_shows_contacts_disappear_after_click_on_delete(page):
    """Le contact disparait apres avoir cliquer sur 'supprimer'"""
    c = Contacts(page)
    c.navigate()
    c.add_contact("Chokri Bourassi", "choukridev18@gmail.com", "0612908518")
    c.delete_contact("Chokri Bourassi")
    assert "Chokri Bourassi" not in c.page.locator(".contact-name").all_inner_texts()
