import pytest
from playwright.sync_api import Page

BASE_URL = "http://localhost:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def app_url() -> str:
    return BASE_URL


@pytest.fixture(autouse=True)
def reset_server(page: Page):
    page.request.post(f"{BASE_URL}/reset")
    yield
