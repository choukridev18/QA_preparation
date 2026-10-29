from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.member_page import MemberPage


def test_connect_page_shows_fields(login_page: LoginPage):
    """page de connexion affiche les champs email et mot de passe et le bouton de connexion."""
    expect(login_page.page.get_by_label("Email professionnel")).to_be_visible()
    expect(login_page.page.get_by_label("Mot de passe")).to_be_visible()
    expect(login_page.page.get_by_role("button", name="Se connecter")).to_be_visible()


def test_invalid_identity_shows_error_message(login_page: LoginPage):
    """identifiants incorrects affichent un message d'erreur"""
    login_page.fill_email("inconnu@hotmail.com")
    login_page.fill_password("123")
    login_page.submit()
    assert login_page.get_error_message() == "Email ou mot de passe incorrect."


def test_valid_login_shows_welcome_with_email(valid_identity: LoginPage):
    """identifiants corrects ouvrent l'espace membre avec message de bienvenue contenant l'email."""
    expect(valid_identity.page).to_have_url(MemberPage.URL)
    m = MemberPage(valid_identity.page)
    assert m.get_welcome_message() == "Bienvenue, employe@interne.fr"


def test_member_without_login_redirects_to_login(page: Page):
    """accès direct à l'espace membre sans être connecté renvoie vers la page de connexion."""
    member = MemberPage(page)
    member.navigate()
    expect(page).to_have_url(f"{LoginPage.URL}/login")


def test_logout_retunrs_to_login(valid_identity: LoginPage):
    """La déconnexion ramène à la page de connexion."""
    logout = MemberPage(valid_identity.page)
    logout.logout()
    expect(valid_identity.page).to_have_url(f"{LoginPage.URL}/login")
