import pytest
from unittest import mock
from src.weather_client import (
    get_temperature,
    get_forecast,
    is_hot,
    CityNotFoundError,
    WeatherAPIError,
)


# ------------------------------------------------------------------ #
# Tests corrects — ils passent dès le départ                          #
# ------------------------------------------------------------------ #


@mock.patch("src.weather_client.get")
def test_get_temperature_success(mock_get):
    """HTTP 200 → returns the correct temperature"""
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 22.5}),
    )
    result = get_temperature("Paris")
    assert result == 22.5


@mock.patch("src.weather_client.get")
def test_is_hot_above_threshold(mock_get):
    """is_hot returns True when temperature > 30"""
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 35.0}),
    )
    assert is_hot("Dubai") is True


@mock.patch("src.weather_client.get")
def test_is_hot_below_threshold(mock_get):
    """is_hot returns False when temperature <= 30"""
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"temperature": 18.0}),
    )
    assert is_hot("Reykjavik") is False


# ------------------------------------------------------------------ #
# Tests avec bugs — à corriger                                         #
# ------------------------------------------------------------------ #


@mock.patch("src.weather_client.get")
def test_get_forecast_success(mock_get):
    """HTTP 200 → returns the correct forecast list"""
    mock_get.return_value = mock.Mock(
        status_code=200,
        json=mock.Mock(return_value={"forecast": [18.0, 20.0, 22.0]}),
    )
    result = get_forecast("Lyon", 3)
    assert result == [18.0, 20.0, 22.0]


@mock.patch("src.weather_client.get")
def test_get_temperature_city_not_found(mock_get):
    """Unknown city → raises the correct exception"""
    mock_get.return_value = mock.Mock(status_code=404)
    with pytest.raises(CityNotFoundError):
        get_temperature("Atlantis")


@mock.patch("src.weather_client.get")
def test_get_temperature_mock_setup(mock_get):
    """HTTP 200 → returns temperature when mock is configured"""
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": 25.0}
    mock_get.return_value = mock_response
    result = get_temperature("Madrid")
    assert result == 25.0


@mock.patch("src.weather_client.get")
def test_get_forecast_json_response(mock_get):
    """HTTP 200 → forecast list is extracted from JSON"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"forecast": [10.0, 12.0, 9.0]}
    result = get_forecast("Oslo", 3)
    assert result == [10.0, 12.0, 9.0]
