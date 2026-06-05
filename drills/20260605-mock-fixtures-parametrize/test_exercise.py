# Lance : pytest test_exercise.py -v

import pytest
from unittest import mock
from exercise import format_message, notify_by_email, notify_by_sms, notify_user, count_successful


# ------------------------------------------------------------------ #
# TODO 1 — format_message                                             #
# ------------------------------------------------------------------ #

@pytest.mark.parametrize("template,name,expected", [
    ("Bonjour {name} !", "Alice", "Bonjour Alice !"),
    ("Bienvenue, {name}.", "Bob", "Bienvenue, Bob."),
    ("{name} a rejoint l'équipe.", "Charlie", "Charlie a rejoint l'équipe."),
])
def test_format_message(template, name, expected):
    assert format_message(template, name) == expected, "Le message n'est pas formaté correctement"


# ------------------------------------------------------------------ #
# TODO 2 — notify_by_email                                            #
# ------------------------------------------------------------------ #

@mock.patch("exercise.send_email_api")
def test_notify_by_email_calls_api_with_correct_args(mock_api, email_user):
    mock_api.return_value = True
    notify_by_email(email_user, "Sujet test", "Corps du message")
    mock_api.assert_called_once_with(email_user.email, "Sujet test", "Corps du message")


@mock.patch("exercise.send_email_api")
def test_notify_by_email_returns_true_on_success(mock_api, email_user):
    mock_api.return_value = True
    assert notify_by_email(email_user, "Sujet", "Corps") is True, "Doit retourner True si l'API réussit"


@mock.patch("exercise.send_email_api")
def test_notify_by_email_returns_false_on_failure(mock_api, email_user):
    mock_api.return_value = False
    assert notify_by_email(email_user, "Sujet", "Corps") is False, "Doit retourner False si l'API échoue"


# ------------------------------------------------------------------ #
# TODO 3 — notify_by_sms                                              #
# ------------------------------------------------------------------ #

@mock.patch("exercise.send_sms_api")
def test_notify_by_sms_calls_api_with_correct_args(mock_api, sms_user):
    mock_api.return_value = True
    notify_by_sms(sms_user, "Votre code est 1234")
    mock_api.assert_called_once_with(sms_user.phone, "Votre code est 1234")


@mock.patch("exercise.send_sms_api")
def test_notify_by_sms_returns_api_result(mock_api, sms_user):
    mock_api.return_value = True
    assert notify_by_sms(sms_user, "Message") is True, "Doit retourner le résultat de send_sms_api"


# ------------------------------------------------------------------ #
# TODO 4 — notify_user                                                #
# ------------------------------------------------------------------ #

@mock.patch("exercise.send_email_api")
def test_notify_user_uses_email_channel(mock_email, email_user):
    mock_email.return_value = True
    result = notify_user(email_user, "Bonjour")
    assert result is True, "notify_user doit retourner True pour un email réussi"
    mock_email.assert_called_once()


@mock.patch("exercise.send_sms_api")
def test_notify_user_uses_sms_channel(mock_sms, sms_user):
    mock_sms.return_value = True
    result = notify_user(sms_user, "Bonjour")
    assert result is True, "notify_user doit retourner True pour un SMS réussi"
    mock_sms.assert_called_once()


# ------------------------------------------------------------------ #
# TODO 5 — count_successful                                           #
# ------------------------------------------------------------------ #

@pytest.mark.parametrize("results,expected", [
    ([True, False, True, True], 3),
    ([False, False, False], 0),
    ([True, True], 2),
    ([], 0),
])
def test_count_successful(results, expected):
    assert count_successful(results) == expected, f"Attendu {expected} succès dans {results}"
