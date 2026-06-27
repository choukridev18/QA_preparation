import re
import pytest
from playwright.sync_api import Page, expect
from pages.signup_page import Step1Page, Step2Page, ConfirmPage


def test_full_signup_flow(page: Page):
    """Inscription complète en 2 étapes → page de confirmation"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Alice Dupont")
    s1.fill_email("alice@example.com")
    s1.fill_password("secret123")
    s1.submit()

    s2 = Step2Page(page)
    expect(page).to_have_url(Step2Page.URL)
    s2.submit()

    expect(page).to_have_url(re.compile(r"/signup/confirm"))


def test_missing_name_shows_error(page: Page):
    """Soumettre l'étape 1 sans nom → message d'erreur"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_email("bob@example.com")
    s1.fill_password("secret123")
    s1.submit()

    error = s1.get_error()
    assert "obligatoire" in error


def test_invalid_email_shows_error(page: Page):
    """Email sans @ → message d'erreur"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Bob Martin")
    s1.fill_email("pasunmail")
    s1.fill_password("secret123")
    s1.submit()

    error = s1.get_error()
    assert "invalide" in error


def test_back_link_goes_to_step1(page: Page):
    """Depuis l'étape 2, cliquer sur Retour → étape 1"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Carol")
    s1.fill_email("carol@example.com")
    s1.fill_password("secret123")
    s1.submit()

    s2 = Step2Page(page)
    expect(page).to_have_url(Step2Page.URL)
    s2.go_back()

    expect(page).to_have_url(Step1Page.URL)


def test_click_on_create_other_count_redirect_step1(page: Page):
    """Cliquer sur 'Créer un autre compte' redirige vers step1"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Choukri")
    s1.fill_email("chouk18@hotmail.com")
    s1.fill_password("12345678")
    s1.submit()
    expect(page).to_have_url(Step2Page.URL)
    s2 = Step2Page(page)
    s2.submit()
    expect(page).to_have_url(f"{ConfirmPage.URL}?name=Choukri")
    cp = ConfirmPage(page)
    cp.click_create_another_count()
    expect(page).to_have_url(Step1Page.URL)


def test_fill_password_less_6_characters(page: Page):
    """Saisir un mot de passe de moins de 6 caractères affiche message erreur"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Choukri")
    s1.fill_email("chouk18@hotmail.com")
    s1.fill_password("1234")
    s1.submit()
    expect(page).to_have_url(Step1Page.URL)
    assert "6 caractères" in s1.get_error()
