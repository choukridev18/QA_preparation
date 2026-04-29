import pytest

from src.weather_client import WeatherClient


@pytest.fixture
def client():
    return WeatherClient(api_key="test-key-123")
