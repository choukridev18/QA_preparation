# Lance : pytest test_exercise.py -v
#
# Ce fichier contient deux sections :
#
#   SECTION A — @mock.patch comme DÉCORATEUR
#     Le mock est injecté comme paramètre de la fonction de test.
#     Syntaxe : @mock.patch("exercise.requests.get")
#               def test_...(mock_get):
#
#   SECTION B — mock.patch comme CONTEXT MANAGER
#     Le mock est disponible dans le bloc `with`.
#     Syntaxe : with mock.patch("exercise.requests.get") as mock_get:
#
#   Les deux font exactement la même chose.
#   Choisis selon la lisibilité et la portée dont tu as besoin.

import pytest
from unittest import mock
from exercise import (
    get_forecast,
    notify_subscriber,
    format_forecast,
    broadcast_forecast,
)


# ============================================================
# SECTION A — @mock.patch (décorateur)
# ============================================================


@mock.patch("exercise.requests.get")
def test_get_forecast_returns_json(mock_get):
    """get_forecast retourne le JSON de la réponse API."""
    mock_get.return_value.json.return_value = {
        "city": "Paris",
        "temp": 22,
        "condition": "ensoleillé",
    }
    result = get_forecast("Paris")
    assert result["city"] == "Paris"
    assert result["temp"] == 22


@mock.patch("exercise.requests.get")
def test_get_forecast_calls_correct_url(mock_get):
    """get_forecast appelle la bonne URL."""
    mock_get.return_value.json.return_value = {
        "city": "Lyon",
        "temp": 18,
        "condition": "nuageux",
    }
    get_forecast("Lyon")
    mock_get.assert_called_once_with("https://api.weather.example.com/v1/Lyon")


@mock.patch("exercise.requests.post")
def test_notify_subscriber_returns_true_on_200(mock_post):
    """notify_subscriber retourne True quand l'API répond 200."""
    mock_post.return_value.status_code = 200
    result = notify_subscriber("alice@example.com", {"city": "Paris", "temp": 22})
    assert result is True, "Doit retourner True pour un statut 200"


@mock.patch("exercise.requests.post")
def test_notify_subscriber_returns_false_on_500(mock_post):
    """notify_subscriber retourne False quand l'API répond 500."""
    mock_post.return_value.status_code = 500
    result = notify_subscriber("alice@example.com", {"city": "Paris", "temp": 22})
    assert result is False, "Doit retourner False pour un statut 500"


@mock.patch("exercise.requests.post")
def test_notify_subscriber_calls_correct_payload(mock_post):
    """notify_subscriber envoie le bon payload à l'API."""
    mock_post.return_value.status_code = 200
    forecast = {"city": "Paris", "temp": 22}
    notify_subscriber("bob@example.com", forecast)
    mock_post.assert_called_once_with(
        "https://api.mailer.example.com/send",
        json={"to": "bob@example.com", "forecast": forecast},
    )


# ============================================================
# SECTION B — with mock.patch(...) (context manager)
# ============================================================


def test_format_forecast_returns_string():
    """format_forecast retourne la chaîne formatée (pas de mock nécessaire)."""
    forecast = {"city": "Lyon", "temp": 18, "condition": "nuageux"}
    assert format_forecast(forecast) == "Lyon: nuageux, 18°C"


def test_get_forecast_with_context_manager():
    """Même test que test_get_forecast_returns_json — syntaxe context manager."""
    with mock.patch("exercise.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "city": "Marseille",
            "temp": 28,
            "condition": "ensoleillé",
        }
        result = get_forecast("Marseille")
        assert result["condition"] == "ensoleillé"


def test_notify_subscriber_with_context_manager():
    """Même test que test_notify_subscriber_returns_true_on_200 — context manager."""
    with mock.patch("exercise.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        result = notify_subscriber("charlie@example.com", {"city": "Nice", "temp": 25})
        assert result is True


def test_broadcast_forecast_returns_success_count():
    """broadcast_forecast retourne le nombre d'envois réussis."""
    with mock.patch("exercise.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "city": "Paris",
            "temp": 22,
            "condition": "ensoleillé",
        }
        with mock.patch("exercise.requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            result = broadcast_forecast("Paris", ["a@ex.com", "b@ex.com", "c@ex.com"])
            assert result == 3, "3 abonnés notifiés avec succès"


def test_broadcast_forecast_calls_get_once():
    """broadcast_forecast appelle get_forecast une seule fois même pour plusieurs abonnés."""
    with mock.patch("exercise.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "city": "Paris",
            "temp": 22,
            "condition": "ensoleillé",
        }
        with mock.patch("exercise.requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            broadcast_forecast("Paris", ["a@ex.com", "b@ex.com"])
            assert (
                mock_get.call_count == 1
            ), "requests.get doit être appelé une seule fois"
            assert (
                mock_post.call_count == 2
            ), "requests.post doit être appelé une fois par abonné"
