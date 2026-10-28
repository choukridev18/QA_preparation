import pytest
import requests
from pages.directory_page import DirectoryPage


BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def reset_data():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")


@pytest.fixture
def directory(page):
    d = DirectoryPage(page)
    d.navigate()
    return d


@pytest.fixture
def directory_after_search(directory: DirectoryPage):
    directory.search("Léa Martin")
    return directory
