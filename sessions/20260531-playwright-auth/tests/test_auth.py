from flask import app
from playwright.sync_api import Page, expect
from pages.auth_page import AuthPage


def test_valid_login_redirects_to_dashboard(page: Page, app_url: str):
    """Login valide → redirection vers le dashboard"""
    auth = AuthPage(page)
    auth.navigate()
    auth.fill_login("admin@example.com", "password123")
    auth.submit()
    expect(page).to_have_url(f"{app_url}/dashboard")


def test_invalid_password_shows_error(page: Page, app_url: str):
    """Mauvais mot de passe → message d'erreur visible"""
    auth = AuthPage(page)
    auth.navigate()
    auth.fill_login("admin@example.com", "mauvais")
    auth.submit()
    expect(page).to_have_url(f"{app_url}/login")
    assert auth.get_error_message() != ""


def test_logout_redirects_to_login(page: Page, app_url: str):
    """Après logout → retour sur la page de login"""
    auth = AuthPage(page)
    auth.navigate()
    auth.fill_login("admin@example.com", "password123")
    auth.submit()
    auth.logout()
    expect(page).to_have_url(f"{app_url}/login")


def test_field_empty_shows_message_error(page: Page, app_url: str):
    """message erreur apparait si champs vide"""
    auth = AuthPage(page)
    auth.navigate()
    auth.submit()
    assert auth.get_error_message() != ""


def test_email_unknown_shows_message_error(page: Page, app_url: str):
    """message erreur apparait email inconnu"""
    auth = AuthPage(page)
    auth.navigate()
    auth.fill_login("chouk18@hotmail.com", "password123")
    auth.submit()
    assert auth.get_error_message() != ""


def test_redirection_login_if_dashboard_without_session(page: Page, app_url: str):
    """redirection page login si adresse dashboard sans session"""
    page.goto(f"{app_url}/dashboard")
    expect(page).to_have_url(f"{app_url}/login")


def test_message_shows_email(page: Page, app_url: str):
    """l'email de l'utilisateur s'affiche apres le login"""
    auth = AuthPage(page)
    auth.navigate()
    auth.fill_login("admin@example.com", "password123")
    auth.submit()
    assert "admin@example.com" in auth.get_welcome_message()
