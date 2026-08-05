import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def reset_slots():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")
