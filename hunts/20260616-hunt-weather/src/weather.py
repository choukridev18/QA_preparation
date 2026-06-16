"""
Client météo — wrapper autour d'une API météo externe.
Récupère les prévisions, formate les données, et envoie des alertes.
"""

import requests

WEATHER_API = "https://api.meteo.example.com/v1"
ALERT_API = "https://api.alerts.example.com/send"


class WeatherError(RuntimeError):
    """Levée quand l'API météo retourne une erreur."""
    pass


def get_forecast(city: str) -> dict:
    """
    Récupère les prévisions météo pour une ville.
    Retourne un dict : {"city": str, "temp": float, "condition": str}
    Lève WeatherError si l'API retourne un statut != 200.
    """
    response = requests.get(f"{WEATHER_API}/forecast/{city}")
    if response.status_code != 200:
        raise WeatherError(f"Impossible de récupérer la météo pour {city}.")
    return response.json()


def format_forecast(forecast: dict) -> str:
    """
    Formate les prévisions en une chaîne lisible.
    Ex : format_forecast({"city": "Paris", "temp": 22.5, "condition": "Ensoleillé"})
      → "Paris : Ensoleillé, 22.5°C"
    """
    return f"{forecast['city']} : {forecast['condition']}, {forecast['temp']}°C"


def send_alert(city: str, message: str) -> bool:
    """
    Envoie une alerte météo pour une ville.
    Retourne True si l'envoi réussit (status 200), False sinon.
    """
    response = requests.post(ALERT_API, json={"city": city, "message": message})
    return response.status_code == 200


def get_temperature(city: str) -> float:
    """
    Retourne uniquement la température pour une ville.
    Utilise get_forecast() en interne.
    Lève WeatherError si la ville est introuvable.
    """
    forecast = get_forecast(city)
    return forecast["temp"]


def is_alert_needed(temp: float, threshold: float = 35.0) -> bool:
    """
    Retourne True si la température dépasse le seuil d'alerte.
    Ex : is_alert_needed(38.0) → True
    """
    return temp >= threshold
