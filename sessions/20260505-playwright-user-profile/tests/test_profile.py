from playwright.sync_api import Page, expect

from pages.profile_page import ProfilePage


def test_update_profile_success(page: Page):
    """Mise à jour avec un nom et un email valides → message de succès visible."""
    p = ProfilePage(page)
    p.navigate()
    p.fill_name("Jean Martin")
    p.fill_email("jean@example.com")
    p.click_save()
    expect(page.locator("#success-message")).to_be_visible()


def test_empty_name_shows_error(page: Page):
    """Soumettre avec le nom vide → message d'erreur visible."""
    p = ProfilePage(page)
    p.navigate()
    p.fill_name("")
    p.fill_email("test@example.com")
    p.click_save()
    expect(page.locator("#error-message")).to_be_visible()


def test_invalid_email_shows_error(page: Page):
    """Email sans @ → message d'erreur visible."""
    p = ProfilePage(page)
    p.navigate()
    p.fill_name("Marie Dupont")
    p.fill_email("pas-un-email")
    p.click_save()
    expect(page.locator("#error-message")).to_be_visible()

def test_check_new_value_after_update(page:Page):
    """Verifier la nouvelle valeur pre-remplie apres mise a jour"""
    p = ProfilePage(page)
    p.navigate()
    p.fill_name("Marie Dupont")
    p.fill_email("marie@example.com")
    p.click_save()
    assert p.get_name_value() == "Marie Dupont"

def test_check_error_message(page:Page):
    """Verifier le contenu exact du message d'erreur"""
    p = ProfilePage(page)
    p.navigate()
    p.fill_name("")
    p.fill_email("marie@example.com")
    p.click_save()
    assert p.get_error_message() == "Le nom est obligatoire."

