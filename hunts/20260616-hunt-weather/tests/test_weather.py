from unittest import mock
import pytest
from src.weather import (
    get_forecast,
    format_forecast,
    send_alert,
    get_temperature,
    is_alert_needed,
    WeatherError,
)


# ── Tests qui passent ──────────────────────────────────────────────────────────


def test_format_forecast_returns_string(forecast_paris):
    result = format_forecast(forecast_paris)
    assert result == "Paris : Ensoleillé, 22.5°C"


def test_is_alert_needed_above_threshold():
    assert is_alert_needed(38.0) is True


def test_is_alert_needed_below_threshold():
    assert is_alert_needed(30.0) is False


# ── Tests avec bugs ────────────────────────────────────────────────────────────


def test_get_forecast_returns_dict():
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "city": "Lyon",
        "temp": 18.0,
        "condition": "Nuageux",
    }

    with mock.patch("requests.get", return_value=mock_response):
        result = get_forecast("Lyon")

    assert result["city"] == "Lyon"


def test_get_forecast_raises_on_error():
    mock_response = mock.MagicMock()
    mock_response.status_code = 500

    with mock.patch("src.weather.requests.get", return_value=mock_response):
        with pytest.raises(WeatherError):
            get_forecast("Inconnue")


def test_send_alert_returns_true_on_success():
    mock_response = mock.MagicMock()
    mock_response.status_code = 200

    with mock.patch("src.weather.requests.post") as mock_post:
        mock_post.return_value = mock_response
        result = send_alert("Nice", "Canicule !")

    assert result is True


def test_get_temperature_calls_get_forecast():
    with mock.patch("src.weather.get_forecast") as mock_fc:
        mock_fc.return_value = {
            "city": "Bordeaux",
            "temp": 25.0,
            "condition": "pluvieux",
        }
        temp = get_temperature("Bordeaux")

    assert temp == 25.0


def test_format_forecast_hot_city(forecast_hot):
    result = format_forecast(forecast_hot)
    assert result == "Séville : Très chaud, 38.0°C"
