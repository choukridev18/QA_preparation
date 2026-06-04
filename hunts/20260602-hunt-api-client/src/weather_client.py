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

    Args:
        city: City name.

    Returns:
        Current temperature in Celsius.

    Raises:
        CityNotFoundError: if the city is not found (HTTP 404).
        WeatherAPIError: if the API returns any other error.
    """
    response = get(f"{BASE_URL}/temperature?city={city}")

    if response.status_code == 404:
        raise CityNotFoundError(f"City not found: {city}")

    if response.status_code != 200:
        raise WeatherAPIError(f"API error: {response.status_code}")

    return response.json()["temperature"]


def get_forecast(city: str, days: int = 3) -> list:
    """
    Fetch a temperature forecast for a city.

    Args:
        city: City name.
        days: Number of days to forecast (default 3).

    Returns:
        List of temperatures for the next `days` days.

    Raises:
        CityNotFoundError: if the city is not found (HTTP 404).
        WeatherAPIError: if the API returns any other error.
    """
    response = get(f"{BASE_URL}/forecast?city={city}&days={days}")

    if response.status_code == 404:
        raise CityNotFoundError(f"City not found: {city}")

    if response.status_code != 200:
        raise WeatherAPIError(f"API error: {response.status_code}")

    return response.json()["forecast"]


def is_hot(city: str, threshold: float = 30.0) -> bool:
    """
    Check whether the current temperature in a city exceeds a threshold.

    Args:
        city: City name.
        threshold: Temperature threshold in Celsius (default 30.0).

    Returns:
        True if temperature > threshold, False otherwise.
    """
    temp = get_temperature(city)
    return temp > threshold
