import pytest
import requests
from pages.login_page import LoginPage

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}


@pytest.fixture(autouse=True)
def reset_data():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page


@pytest.fixture
def valid_identity(login_page: LoginPage):
    login_page.fill_email("employe@interne.fr")
    login_page.fill_password("qa-demo")
    login_page.submit()
    return login_page
