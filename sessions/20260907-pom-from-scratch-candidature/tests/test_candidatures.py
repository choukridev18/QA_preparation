from playwright.sync_api import Page, expect
from pages.candidatures_page import Step1Page, Step2Page, ConfirmationPage

url = "http://127.0.0.1:5001"


def test_fill_informations_valide(page: Page, fill_valide_informations):
    expect(page).to_have_url(f"{url}/step2")


def test_fill_informations_with_phone_field_empty(page: Page):
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("choukri")
    s1.fill_email("testeur@test.com")
    s1.fill_number_phone("")
    s1.submit()
    assert s1.get_message_error() == "Le téléphone est obligatoire."


def test_fill_informations_with_email_invalide(page: Page):
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("choukri")
    s1.fill_email("testeurtest.com")
    s1.fill_number_phone("0612908519")
    s1.submit()
    assert s1.get_message_error() == "L'adresse email est invalide."


def test_complete_step2page(page: Page, fill_step2page):
    expect(page).to_have_url(f"{url}/confirmation")


def test_name_and_position_candidate_affiched(page: Page, fill_step2page):
    c = ConfirmationPage(page)
    assert "Chokri Bourassi" in c.message_success()
    assert "a bien été reçue" in c.message_success()
