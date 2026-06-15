import pytest
from playwright.sync_api import Page, expect
from pages.multistep_page import Step1Page, Step2Page, ConfirmPage


def test_step1_empty_first_name_shows_error(page: Page):
    """Soumettre l'étape 1 sans prénom affiche une erreur inline."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_last_name("Dupont")
    s1.fill_email("alice@example.com")
    s1.submit()

    expect(page).to_have_url(Step1Page.URL)
    assert s1.get_first_name_error() == "Le prénom est requis."


def test_step1_invalid_email_shows_error(page: Page):
    """Un email sans '@' affiche une erreur inline."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Alice")
    s1.fill_last_name("Dupont")
    s1.fill_email("pasunemail")
    s1.submit()

    expect(page).to_have_url(Step1Page.URL)
    assert s1.get_email_error() == "Un email valide est requis."


def test_step1_valid_navigates_to_step2(page: Page):
    """L'étape 1 valide redirige vers l'étape 2."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Alice")
    s1.fill_last_name("Dupont")
    s1.fill_email("alice@example.com")
    s1.submit()

    expect(page).to_have_url(Step2Page.URL)


def test_step2_no_plan_shows_error(page: Page):
    """Soumettre l'étape 2 sans plan affiche une erreur inline."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Alice")
    s1.fill_last_name("Dupont")
    s1.fill_email("alice@example.com")
    s1.submit()

    s2 = Step2Page(page)
    s2.submit()

    expect(page).to_have_url(Step2Page.URL)
    assert s2.get_plan_error() == "Choisissez un plan valide."


def test_full_flow_reaches_success(page: Page):
    """Le parcours complet (étapes 1→2→3→succès) affiche la page de succès."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Alice")
    s1.fill_last_name("Dupont")
    s1.fill_email("alice@example.com")
    s1.submit()

    s2 = Step2Page(page)
    s2.select_plan("Pro")
    s2.submit()

    confirm = ConfirmPage(page)
    expect(page).to_have_url(ConfirmPage.URL)
    assert confirm.get_first_name() == "Alice"
    assert confirm.get_plan() == "Pro"
    confirm.confirm()

    expect(page).to_have_url("http://localhost:5001/success")


def test_step2_back_button_returns_to_step1(page: Page):
    """Le bouton 'Retour' de l'étape 2 renvoie à l'étape 1."""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Alice")
    s1.fill_last_name("Dupont")
    s1.fill_email("alice@example.com")
    s1.submit()

    s2 = Step2Page(page)
    s2.go_back()

    expect(page).to_have_url(Step1Page.URL)


def test_confirm_page_shows_last_name(page: Page):
    """Le nom est affiché sur la page de confirmation"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("Choukri")
    s1.fill_last_name("Bouras")
    s1.fill_email("chouk@example.com")
    s1.submit()
    s2 = Step2Page(page)
    s2.select_plan("Gratuit")
    s2.submit()
    confirm = ConfirmPage(page)
    expect(page).to_have_url(confirm.URL)
    assert confirm.get_last_name() == "Bouras"


def test_submit_step1_with_all_fields_empty_shows_error_messages(page: Page):
    """Soumettre etape 1 avec les champs vides pour voir les messages erreurs"""
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_first_name("")
    s1.fill_last_name("")
    s1.fill_email("")
    s1.submit()
    errors = s1.get_all_errors()
    assert len(errors) == 3
