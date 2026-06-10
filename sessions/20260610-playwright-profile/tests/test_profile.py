import pytest
from playwright.sync_api import Page, expect
from pages.profile_page import ProfilePage, EditProfilePage


def test_profile_displays_default_info(page: Page):
    """La page profil affiche les informations par défaut."""
    p = ProfilePage(page)
    p.navigate()
    assert p.get_name() == "Alice Martin"
    assert p.get_email() == "alice@example.com"


def test_edit_link_goes_to_edit_page(page: Page):
    """Cliquer sur 'Modifier le profil' redirige vers le formulaire d'édition."""
    p = ProfilePage(page)
    p.navigate()
    p.go_to_edit()
    expect(page).to_have_url("http://localhost:5001/profile/edit")


def test_valid_update_shows_success_message(page: Page):
    """Un formulaire valide enregistre les données et affiche le message de succès."""
    edit = EditProfilePage(page)
    edit.navigate()
    edit.fill_name("Bob Dupont")
    edit.fill_email("bob@example.com")
    edit.fill_bio("Testeur QA junior.")
    edit.submit()

    profile = ProfilePage(page)
    expect(page).to_have_url("http://localhost:5001/profile")
    assert profile.has_success_message()
    assert profile.get_name() == "Bob Dupont"


def test_empty_name_shows_error(page: Page):
    """Soumettre le formulaire avec un nom vide affiche une erreur inline."""
    edit = EditProfilePage(page)
    edit.navigate()
    edit.fill_name("")
    edit.fill_email("bob@example.com")
    edit.submit()

    expect(page).to_have_url("http://localhost:5001/profile/edit")
    assert edit.get_name_error() == "Le nom est requis."


def test_invalid_email_shows_error(page: Page):
    """Un email sans '@' affiche une erreur inline sur le champ email."""
    edit = EditProfilePage(page)
    edit.navigate()
    edit.fill_name("Bob Dupont")
    edit.fill_email("pasunemail")
    edit.submit()

    expect(page).to_have_url("http://localhost:5001/profile/edit")
    assert edit.get_email_error() == "L'email n'est pas valide."


def test_click_button_cancel(page: Page):
    """Cliquer sur Annuler depuis le formulaire ramène sur la page profil."""
    p = ProfilePage(page)
    p.navigate()
    p.go_to_edit()
    expect(page).to_have_url("http://localhost:5001/profile/edit")
    edit = EditProfilePage(page)
    edit.click_cancel()
    expect(page).to_have_url("http://localhost:5001/profile")


def test_email_empty_shows_message_error(page: Page):
    """Quand le champs email est vide, un message d'erreur apparait"""
    p = ProfilePage(page)
    p.navigate()
    p.go_to_edit()
    edit = EditProfilePage(page)
    edit.fill_name("Bob Dupont")
    edit.fill_email("")
    edit.fill_bio("Testeur QA junior.")
    edit.submit()
    assert edit.get_email_error() == "L'email est requis."
