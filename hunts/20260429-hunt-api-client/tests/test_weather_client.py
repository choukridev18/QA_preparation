from multiprocessing import Value
import pytest
from unittest.mock import MagicMock, patch

from src.weather_client import WeatherClient


# ---------------------------------------------------------------
# Tests corrects — ceux-ci passent déjà
# ---------------------------------------------------------------

def test_get_temperature_returns_dict(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"city": "Lyon", "temp": 18.5}
        result = client.get_temperature("Lyon")
    assert isinstance(result, dict)
    assert "temp_celsius" in result
    assert result["unit"] == "celsius"


def test_get_alerts_empty_on_404(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        result = client.get_alerts("VilleInconnue")
    assert result == []


def test_forecast_days_out_of_range(client):
    with patch("src.weather_client.requests.get"):
        with pytest.raises(ValueError):
            client.get_forecast("Paris", days=0)


# ---------------------------------------------------------------
# Tests avec bugs intentionnels — à corriger
# ---------------------------------------------------------------

def test_get_temperature_city_name(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"city": "Paris", "temp": 22.0}
        result = client.get_temperature("Paris")
    assert result["city"] == "Paris"  # BUG 1


def test_get_temperature_empty_city(client):
    with pytest.raises(ValueError):  # BUG 2
        client.get_temperature("")


def test_get_temperature_server_error(client):
    with patch("src.weather_client.requests.get") as mock_get:
        with pytest.raises(ConnectionError):
            mock_get.return_value.status_code = 500
            client.get_temperature("Paris")
         # BUG 3


def test_get_forecast_returns_sorted_conditions(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value ={"conditions": ["nuageux", "ensoleillé", "pluvieux"]} # BUG 4
        mock_get.return_value = mock_response
        result = client.get_forecast("Bordeaux", days=3)
    assert result == ["ensoleillé", "nuageux", "pluvieux"]


def test_get_forecast_unsorted_input(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "conditions": ["brumeux", "ensoleillé","venteux" ],
        }
        result = client.get_forecast("Marseille", days=2)
    assert result == ["brumeux", "ensoleillé","venteux"]  # BUG 5
