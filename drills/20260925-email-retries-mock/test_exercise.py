# Lance : pytest test_exercise.py -v

from unittest.mock import patch

import pytest

from exercise import (
    DeliveryError,
    EmailError,
    EmailMessage,
    build_payload,
    count_failed_attempts,
    notify_user,
    send_email,
    send_with_retry,
    validate_recipient,
)


# --- validate_recipient -------------------------------------------------------


def test_validate_recipient_strip_and_keep():
    assert validate_recipient("  alice@saas.io  ") == "alice@saas.io"


@pytest.mark.parametrize(
    "bad_email",
    ["", "   ", "pas-un-email", "alice.saas.io"],
)
def test_validate_recipient_invalide_leve_email_error(bad_email):
    with pytest.raises(EmailError):
        validate_recipient(bad_email)


# --- build_payload ------------------------------------------------------------


def test_build_payload_structure(welcome_message):
    payload = build_payload(welcome_message)
    assert payload == {
        "to": "new.user@saas.io",
        "subject": "Bienvenue",
        "body": "Votre compte est prêt.",
        "priority": "normal",
    }, "Le payload doit contenir to, subject, body et priority='normal'"


# --- send_email (return_value + assert_called_with) ---------------------------


def test_send_email_retourne_la_reponse_api(welcome_message, api_ok_response):
    with patch("exercise.call_mail_api", return_value=api_ok_response) as mock_api:
        result = send_email(welcome_message)

    assert result == api_ok_response
    mock_api.assert_called_with(
        {
            "to": "new.user@saas.io",
            "subject": "Bienvenue",
            "body": "Votre compte est prêt.",
            "priority": "normal",
        }
    )


def test_send_email_propage_connection_error(welcome_message):
    with patch(
        "exercise.call_mail_api",
        side_effect=ConnectionError("timeout"),
    ):
        with pytest.raises(ConnectionError):
            send_email(welcome_message)


def test_send_email_refuse_destinataire_invalide():
    msg = EmailMessage(to="invalide", subject="X", body="Y")
    with pytest.raises(EmailError):
        send_email(msg)


# --- send_with_retry (side_effect liste) --------------------------------------


def test_send_with_retry_reussit_au_2e_essai(welcome_message, api_ok_response):
    """Premier appel API échoue, second réussit — comme mercredi."""
    with patch(
        "exercise.call_mail_api",
        side_effect=[ConnectionError("timeout"), api_ok_response],
    ) as mock_api:
        result = send_with_retry(welcome_message, max_attempts=3)

    assert result == api_ok_response
    assert mock_api.call_count == 2


def test_send_with_retry_epuise_leve_delivery_error(welcome_message):
    with patch(
        "exercise.call_mail_api",
        side_effect=ConnectionError("down"),
    ):
        with pytest.raises(DeliveryError, match="max retries exceeded"):
            send_with_retry(welcome_message, max_attempts=3)


# --- notify_user --------------------------------------------------------------


def test_notify_user_retourne_sent_id(api_ok_response):
    with patch("exercise.call_mail_api", return_value=api_ok_response):
        assert notify_user("bob@saas.io", "Hi", "Hello") == "sent:msg-42"


def test_notify_user_email_invalide_sans_appeler_api():
    with patch("exercise.call_mail_api") as mock_api:
        with pytest.raises(EmailError):
            notify_user("pas-bon", "Hi", "Hello")
        mock_api.assert_not_called()


# --- count_failed_attempts ----------------------------------------------------


@pytest.mark.parametrize(
    "results, expected",
    [
        ([], 0),
        ([True, True], 0),
        ([False, False, False], 3),
        ([True, False, True, False, False], 3),
    ],
)
def test_count_failed_attempts(results, expected):
    assert count_failed_attempts(results) == expected
