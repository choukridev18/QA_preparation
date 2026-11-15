import pytest

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def reset_server(page):
    page.request.post(f"{BASE_URL}/reset")
    yield
    page.request.post(f"{BASE_URL}/reset")