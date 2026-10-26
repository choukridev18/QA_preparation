from playwright.sync_api import Page, expect
from pages.leave_page import LeaveFormPage
from pages.confirmation_page import ConfirmationPage

URL = "http://127.0.0.1:5001"


def test_whole_request_shows_confirmation(request_leave_valid: ConfirmationPage):
    expect(request_leave_valid.page).to_have_url(f"{URL}/confirmation")
    assert request_leave_valid.get_message_leaving_recorded() == "Demande enregistrée"


def test_confirmation_page_shows_dates_and_reason(
    request_leave_valid: ConfirmationPage,
):
    assert request_leave_valid.get_message_confirmation_start_date() == "2026-11-10"
    assert request_leave_valid.get_message_confirmation_end_date() == "2026-12-22"
    assert request_leave_valid.get_message_confirmation_reason() == "Vacances"


def test_field_missed_shows_error_message(leave: LeaveFormPage):
    leave.fill_start_date("2026-11-10")
    leave.fill_end_date("2026-12-22")
    leave.fill_reason("")
    leave.click_submit_form()
    expect(leave.page).to_have_url(f"{URL}/")
    assert leave.get_error_message() == "Le motif est obligatoire."


def test_invalid_dates_shows_error_message(leave: LeaveFormPage):
    leave.fill_start_date("2026-12-25")
    leave.fill_end_date("2026-11-25")
    leave.fill_reason("Vacances")
    leave.click_submit_form()
    expect(leave.page).to_have_url(f"{URL}/")
    assert (
        leave.get_error_message() == "La date de fin doit être après la date de début."
    )


def test_open_confirmation_page_directly_redirect_leave_page(page):
    c = ConfirmationPage(page)
    c.navigate()
    expect(c.page).to_have_url(f"{URL}/")
