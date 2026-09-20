from playwright.sync_api import Page, expect

from pages.preferences_page import PreferencesPage

URL = "http://127.0.0.1:5001"


def test_save_preferences_success(page: Page):
    """Enregistrement valide : message de succès + résumé affiché."""
    prefs = PreferencesPage(page)
    prefs.navigate()
    prefs.fill_email("alice@exemple.com")
    prefs.check_category("Technologie")
    prefs.check_category("Culture")
    prefs.select_frequency("Hebdomadaire")
    prefs.submit()

    expect(page.get_by_role("status")).to_contain_text("Préférences enregistrées")
    assert prefs.get_saved_email() == "alice@exemple.com"
    expect(page.locator("#saved-categories")).to_contain_text("Technologie")
    expect(page.locator("#saved-frequency")).to_have_text("Hebdomadaire")


def test_error_when_no_category(page: Page):
    """Sans catégorie cochée : message d'erreur visible."""
    prefs = PreferencesPage(page)
    prefs.navigate()
    prefs.fill_email("bob@exemple.com")
    prefs.select_frequency("Mensuelle")
    prefs.submit()

    expect(page.get_by_role("alert")).to_be_visible()
    assert "catégorie" in prefs.get_error_message().lower()


def test_error_when_email_missing(page: Page):
    """Sans email : message d'erreur obligatoire."""
    prefs = PreferencesPage(page)
    prefs.navigate()
    prefs.check_category("Sport")
    prefs.select_frequency("Quotidienne")
    prefs.submit()

    expect(page.get_by_role("alert")).to_be_visible()
    assert "email" in prefs.get_error_message().lower()


def test_error_when_frequency_is_not_checked(page: Page):
    """Message erreur sans frequence selecionné"""
    prefs = PreferencesPage(page)
    prefs.navigate()
    prefs.fill_email("bob@exemple.com")
    prefs.check_category("Technologie")
    prefs.submit()
    assert prefs.get_error_message() == "Choisissez une fréquence"


def test_saved_preferences_appear_on_summary(page: Page):
    """Après un enregistrement valide,'summary' affiche les mêmes données."""
    prefs = PreferencesPage(page)
    prefs.navigate()
    prefs.fill_email("bob@exemple.com")
    prefs.check_category("Technologie")
    prefs.select_frequency("Quotidienne")
    prefs.submit()
    prefs.go_to_summary()
    expect(page).to_have_url(f"{URL}/summary")
    expect(page.locator("#summary-email")).to_have_text("bob@exemple.com")
    expect(page.locator("#summary-categories")).to_have_text("Technologie")
    expect(page.locator("#summary-frequency")).to_have_text("Quotidienne")
