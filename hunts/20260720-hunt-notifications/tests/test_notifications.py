import pytest
from unittest import mock
from src.notifications import (
    calculate_priority,
    send_alert,
    format_message,
    get_priority_label,
    create_notification,
)


# --- Tests corrects (passent dès le départ) ---


def test_format_message_with_valid_data():
    result = format_message(
        "Alerte pour {user} : {event}", {"user": "Alice", "event": "CPU élevé"}
    )
    assert result == "Alerte pour Alice : CPU élevé"


def test_get_priority_label_returns_low():
    assert get_priority_label(1.5) == "low"


def test_get_priority_label_returns_high():
    assert get_priority_label(8.0) == "high"


# --- Tests avec bugs ---


def test_calculate_priority_returns_correct_score():
    result = calculate_priority(0.7, 0.4)
    assert result == pytest.approx(0.28)  # BUG 1


@mock.patch("src.notifications.requests.post")  # BUG 2
def test_send_alert_calls_external_api(mock_post):
    mock_post.return_value.status_code = 200
    result = send_alert("alice@example.com", "Alerte critique")
    mock_post.assert_called_once()


def test_create_notification_raises_on_empty_user_id():
    with pytest.raises(ValueError):  # BUG 3
        create_notification("", "Test", 0.5, 0.8)


def test_priority_score_stored_in_notification(sample_notification):
    assert sample_notification["priority_score"] == pytest.approx(0.72)  # BUG 4
