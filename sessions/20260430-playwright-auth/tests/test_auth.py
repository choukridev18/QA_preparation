from multiprocessing import connection
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login_redirects_to_dashboard(page: Page):
    """Une connexion avec des identifiants valides redirige vers /dashboard."""
    login = LoginPage(page)
    login.navigate()
    login.login("alice@example.com", "password123")
    expect(page).to_have_url("http://localhost:5001/dashboard")


def test_invalid_login_shows_error(page: Page):
    """Un mauvais mot de passe affiche un message d'erreur sur la page de login."""
    login = LoginPage(page)
    login.navigate()
    login.login("alice@example.com", "mauvais-mdp")
    error = login.get_error_message()
    assert error is not None
    assert "Identifiants incorrects" in error


def test_dashboard_redirects_to_login_when_not_authenticated(page: Page):
    """Accéder à /dashboard sans être connecté redirige vers /login."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    expect(page).to_have_url("http://localhost:5001/login")


def test_dashboard_shows_welcome_message(page: Page):
    """ Un message de bienvenue avec l'email de l utilisateur doit s'afficher apres Connexion"""
    login = LoginPage(page)
    login.navigate()
    login.login("alice@example.com", "password123")
    dashboard = DashboardPage(page)
    message = dashboard.get_welcome_message()
    assert "alice@example.com" in message

def test_dashboard_redirects_to_login_when_disconnected(page:Page):
    """Une deconnexion redirige vers /login """
    login = LoginPage(page)
    login.navigate()
    login.login("alice@example.com", "password123")
    dashboard = DashboardPage(page)
    dashboard.logout()
    expect(page).to_have_url("http://localhost:5001/login")


