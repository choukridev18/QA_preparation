import pytest
from unittest import mock
from src.weather_client import (
    get_temperature,
    get_forecast,
    is_hot,
    CityNotFoundError,
    WeatherAPIError,
)


# --- corrects (ne pas casser) ---


@mock.patch("src.weather_client.get")
def test_get_temperature_success(mock_get):
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 22.5}),
    )
    assert get_temperature("Paris") == 22.5


@mock.patch("src.weather_client.get")
def test_is_hot_above_threshold(mock_get):
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 35.0}),
    )
    assert is_hot("Dubai") is True


@mock.patch("src.weather_client.get")
def test_is_hot_below_threshold(mock_get):
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 12.0}),
    )
    assert is_hot("Oslo") is False


# --- 1 bug par test ---


@mock.patch("src.weather_client.get")
def test_get_forecast_success(mock_get):
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"forecast": [18.0, 20.0, 22.0]}),
    )
    assert get_forecast("Lyon", 3) == [18.0, 20.0, 22.0]


@mock.patch("src.weather_client.get")
def test_get_temperature_city_not_found(mock_get):
    mock_get.return_value = mock.Mock(status_code=404)
    with pytest.raises(CityNotFoundError):
        get_temperature("Atlantis")


@mock.patch("src.weather_client.get")
def test_get_temperature_from_mock_response(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 25.0}
    mock_get.return_value = mock_response
    assert get_temperature("Madrid") == 25.0


@mock.patch("src.weather_client.get")
def test_get_temperature_uses_fixture(mock_get, mock_http_200):
    mock_http_200.json.return_value = {"temperature": 19.0}
    mock_get.return_value = mock_http_200
    assert get_temperature("Nantes") == 19.0
