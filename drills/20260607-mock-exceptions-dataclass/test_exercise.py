# Lance : pytest test_exercise.py -v

import pytest
import requests
from unittest import mock
from exercise import (
    Notification,
    NotificationError,
    create_notification,
    send_notification,
    send_notification_safe,
    send_all,
    is_valid_recipient,
)


# -------------------------------------------------------
# TODO 1 — create_notification
# -------------------------------------------------------

def test_create_notification_returns_dataclass(notif):
    """create_notification retourne bien un objet Notification."""
    result = create_notification("alice@example.com", "Bienvenue", "Bonjour Alice, bienvenue sur la plateforme.")
    assert isinstance(result, Notification), "Le résultat doit être une Notification"
    assert result == notif, "Les champs doivent correspondre aux arguments"


# -------------------------------------------------------
# TODO 2 — send_notification
# -------------------------------------------------------

@mock.patch("exercise.requests.post")
def test_send_notification_returns_true_on_200(mock_post, notif):
    """send_notification retourne True quand l'API répond 200."""
    mock_post.return_value.status_code = 200
    assert send_notification(notif) is True, "Doit retourner True pour un statut 200"


@mock.patch("exercise.requests.post")
def test_send_notification_returns_false_on_error(mock_post, notif):
    """send_notification retourne False quand l'API répond 500."""
    mock_post.return_value.status_code = 500
    assert send_notification(notif) is False, "Doit retourner False pour un statut 500"


@mock.patch("exercise.requests.post")
def test_send_notification_calls_correct_url(mock_post, notif):
    """send_notification appelle la bonne URL avec le bon payload."""
    mock_post.return_value.status_code = 200
    send_notification(notif)
    mock_post.assert_called_once_with(
        "https://api.notify.example.com/send",
        json={"to": notif.recipient, "subject": notif.subject, "body": notif.body},
    )


# -------------------------------------------------------
# TODO 3 — send_notification_safe
# -------------------------------------------------------

@mock.patch("exercise.requests.post")
def test_send_notification_safe_raises_on_connection_error(mock_post, notif):
    """send_notification_safe lève NotificationError si l'API est injoignable."""
    mock_post.side_effect = requests.ConnectionError()
    with pytest.raises(NotificationError, match="indisponible"):
        send_notification_safe(notif)


@mock.patch("exercise.requests.post")
def test_send_notification_safe_returns_true_on_200(mock_post, notif):
    """send_notification_safe retourne True quand l'API répond 200."""
    mock_post.return_value.status_code = 200
    assert send_notification_safe(notif) is True


# -------------------------------------------------------
# TODO 4 — send_all
# -------------------------------------------------------

@mock.patch("exercise.requests.post")
def test_send_all_returns_count_of_successes(mock_post, notif_list):
    """send_all retourne le nombre d'envois réussis."""
    mock_post.return_value.status_code = 200
    assert send_all(notif_list) == 3, "3 notifications sur 3 doivent réussir"


@mock.patch("exercise.requests.post")
def test_send_all_counts_only_successes(mock_post, notif_list):
    """send_all ne compte que les réponses 200."""
    mock_post.return_value.status_code = 500
    assert send_all(notif_list) == 0, "Aucune notification ne doit réussir avec statut 500"


# -------------------------------------------------------
# TODO 5 — is_valid_recipient
# -------------------------------------------------------

@pytest.mark.parametrize("email,attendu", [
    ("alice@example.com", True),
    ("bob@sub.domain.org", True),
    ("pas-un-email", False),
    ("", False),
    ("manque-arobase.com", False),
    ("@nodomain", False),
    ("no-dot@nodot", False),
])
def test_is_valid_recipient(email, attendu):
    assert is_valid_recipient(email) == attendu, f"{email!r} → attendu {attendu}"
