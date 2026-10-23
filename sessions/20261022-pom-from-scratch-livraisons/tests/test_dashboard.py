from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage


URL = "http://127.0.0.1:5001"


def test_shows_5_deliveries(dashboard: DashboardPage):
    assert dashboard.get_total_deliveries() == 5


def test_filter_in_progress_shows_only_in_progress(dashboard: DashboardPage):
    dashboard.filter_by("En cours")
    assert dashboard.get_row_count() == 3


def test_counter_shows_right_number(dashboard: DashboardPage):
    result = dashboard.get_count_en_cours()
    assert result == 3


def test_change_status_delivery(dashboard: DashboardPage):
    dashboard.update_status(2, "retourné")
    assert "retourné" in dashboard.get_status(2)


def test_counter_update_after_status_change(dashboard: DashboardPage):
    dashboard.update_status(1, "livré")
    assert dashboard.get_count_en_cours() == 2
