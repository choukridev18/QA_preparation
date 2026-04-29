import requests


class WeatherClient:
    """Client pour l'API météo MeteoExample.

    Toutes les méthodes lèvent des exceptions claires en cas d'entrée invalide
    ou d'erreur serveur.
    """

    BASE_URL = "https://api.meteo-example.com/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_temperature(self, city: str) -> dict:
        """Retourne la température actuelle pour une ville.

        Returns:
            {"city": str, "temp_celsius": float, "unit": "celsius"}

        Raises:
            ValueError: si city est une chaîne vide
            ConnectionError: si l'API répond avec un statut 500
        """
        if not city:
            raise ValueError("Le nom de la ville ne peut pas être vide")
        response = requests.get(
            f"{self.BASE_URL}/temperature",
            params={"city": city, "key": self.api_key},
        )
        if response.status_code == 500:
            raise ConnectionError("Erreur serveur API météo")
        data = response.json()
        return {
            "city": data["city"],
            "temp_celsius": round(data["temp"], 2),
            "unit": "celsius",
        }

    def get_forecast(self, city: str, days: int = 3) -> list[str]:
        """Retourne les conditions météo prévues, triées alphabétiquement.

        Returns:
            Liste de conditions triées (ex: ["brumeux", "ensoleillé", "venteux"])

        Raises:
            ValueError: si days < 1 ou days > 7
        """
        if days < 1 or days > 7:
            raise ValueError("Le nombre de jours doit être entre 1 et 7")
        response = requests.get(
            f"{self.BASE_URL}/forecast",
            params={"city": city, "days": days, "key": self.api_key},
        )
        data = response.json()
        return sorted(data["conditions"])

    def get_alerts(self, city: str) -> list[dict]:
        """Retourne les alertes météo actives pour une ville.

        Returns:
            Liste d'alertes (liste vide si aucune alerte ou ville inconnue)
        """
        response = requests.get(
            f"{self.BASE_URL}/alerts",
            params={"city": city, "key": self.api_key},
        )
        if response.status_code == 404:
            return []
        return response.json().get("alerts", [])
