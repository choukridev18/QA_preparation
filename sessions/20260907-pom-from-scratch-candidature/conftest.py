import pytest
import requests
from pages.candidatures_page import Step1Page, Step2Page, ConfirmationPage

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def reset_session():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")


@pytest.fixture
def fill_valide_informations(page):
    s1 = Step1Page(page)
    s1.navigate()
    s1.fill_name("Chokri Bourassi")
    s1.fill_email("testeur@test.com")
    s1.fill_number_phone("0612908519")
    s1.submit()
    return s1


@pytest.fixture
def fill_step2page(page, fill_valide_informations):
    s2 = Step2Page(page)
    s2.navigate()
    s2.choice_position("QA Engineer")
    s2.experiences_years("3 à 5 ans")
    s2.motivation("j'aimerais apporter mon experience a vos services.")
    s2.submit()
    return s2
