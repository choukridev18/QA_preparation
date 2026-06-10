# ============================================================
# DRILL — mock.patch décorateur · mock.patch context manager
#         return_value · side_effect · assert_called_with
# ============================================================
# Contexte :
#   Service de météo qui appelle une API externe pour récupérer
#   les prévisions et notifier les abonnés par email.
#   Les tests mockent l'API pour ne jamais faire de vrais appels réseau.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
#
# À lire dans test_exercise.py avant de commencer :
#   - Section A : tests avec @mock.patch (décorateur)
#   - Section B : tests avec `with mock.patch(...)` (context manager)
#   Les deux font la même chose — la syntaxe seule diffère.
# ============================================================

import requests

WEATHER_API = "https://api.weather.example.com/v1"
MAILER_API = "https://api.mailer.example.com/send"


# ------------------------------------------------------------
# TODO 1 — Récupérer les prévisions météo d'une ville
# ------------------------------------------------------------
# Appelle GET {WEATHER_API}/{city}
# Retourne le JSON de la réponse (un dict)
# Entrée  : "Paris"
# Sortie  : {"city": "Paris", "temp": 22, "condition": "ensoleillé"}
# ------------------------------------------------------------
def get_forecast(city: str) -> dict:
    return requests.get(f"{WEATHER_API}/{city}").json()


# ------------------------------------------------------------
# TODO 2 — Notifier un abonné
# ------------------------------------------------------------
# Appelle POST {MAILER_API} avec json={"to": email, "forecast": forecast}
# Retourne True si le statut HTTP est 200, False sinon
# Entrée  : "alice@example.com", {"city": "Paris", "temp": 22}
# Sortie  : True (si 200) ou False (si autre)
# ------------------------------------------------------------
def notify_subscriber(email: str, forecast: dict) -> bool:
    create = requests.post(f"{MAILER_API}", json={"to": email, "forecast": forecast})
    return create.status_code == 200


# ------------------------------------------------------------
# TODO 3 — Formater les prévisions pour affichage
# ------------------------------------------------------------
# Entrée  : {"city": "Lyon", "temp": 18, "condition": "nuageux"}
# Sortie  : "Lyon: nuageux, 18°C"
# (pas d'appel réseau — pas de mock nécessaire)
# ------------------------------------------------------------
def format_forecast(forecast: dict) -> str:
    return f"{forecast["city"]}: {forecast["condition"]}, {forecast["temp"]}°C"


# ------------------------------------------------------------
# TODO 4 — Diffuser les prévisions à plusieurs abonnés
# ------------------------------------------------------------
# Appelle get_forecast(city) une fois
# Puis notify_subscriber(email, forecast) pour chaque email
# Retourne le nombre d'envois réussis (ceux qui retournent True)
# Entrée  : "Paris", ["a@ex.com", "b@ex.com"]
# Sortie  : 2 (si les deux réussissent)
# ------------------------------------------------------------
def broadcast_forecast(city: str, emails: list[str]) -> int:
    forecast = get_forecast(city)
    compteur = 0
    for email in emails:
        if notify_subscriber(email, forecast):
            compteur += 1
    return compteur
