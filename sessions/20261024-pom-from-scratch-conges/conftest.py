import pytest
import requests
from pages.leave_page import LeaveFormPage
from pages.confirmation_page import ConfirmationPage

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(autouse=True)
def data_reset():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")


@pytest.fixture
def leave(page):
    l = LeaveFormPage(page)
    l.navigate()
    return l


@pytest.fixture
def request_leave_valid(leave):
    leave.fill_start_date("2026-11-10")
    leave.fill_end_date("2026-12-22")
    leave.fill_reason("Vacances")
    leave.click_submit_form()
    return ConfirmationPage(leave.page)
