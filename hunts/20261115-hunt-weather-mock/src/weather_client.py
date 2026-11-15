from requests import get

BASE_URL = "https://api.weather.example.com"


class CityNotFoundError(Exception):
    """Raised when the requested city is not found by the API."""
    pass


class WeatherAPIError(Exception):
    """Raised when the API returns an unexpected error."""
    pass


def get_temperature(city: str) -> float:
    """
    Fetch the current temperature for a city.

    Raises:
        CityNotFoundError: HTTP 404.
        WeatherAPIError: any other non-200 status.
    """
    response = get(f"{BASE_URL}/temperature?city={city}")

    if response.status_code == 404:
        raise CityNotFoundError(f"City not found: {city}")

    if response.status_code != 200:
        raise WeatherAPIError(f"API error: {response.status_code}")

    return response.json()["temperature"]


def get_forecast(city: str, days: int = 3) -> list:
    """Fetch a list of daily temperatures for the next `days` days."""
    response = get(f"{BASE_URL}/forecast?city={city}&days={days}")

    if response.status_code == 404:
        raise CityNotFoundError(f"City not found: {city}")

    if response.status_code != 200:
        raise WeatherAPIError(f"API error: {response.status_code}")

    return response.json()["forecast"]


def is_hot(city: str, threshold: float = 30.0) -> bool:
    """True when current temperature is strictly above `threshold`."""
    temp = get_temperature(city)
    return temp > threshold