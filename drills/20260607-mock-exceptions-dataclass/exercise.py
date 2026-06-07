# ============================================================
# DRILL — mock.patch · side_effect · exceptions custom · dataclass · pytest.raises
# ============================================================
# Contexte :
#   Tu travailles sur un service d'envoi de notifications pour une plateforme SaaS.
#   Le service appelle une API externe pour envoyer des emails.
#   Quand l'API est indisponible, le service doit lever une exception métier claire.
#   Les tests mockent l'API pour ne jamais faire de vrais appels réseau.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

from dataclasses import dataclass
import json
import requests


# ============================================================
# Dataclass — à utiliser telle quelle, ne pas modifier
# ============================================================


@dataclass
class Notification:
    recipient: str  # adresse email du destinataire
    subject: str  # sujet du message
    body: str  # corps du message


# ============================================================
# Exception personnalisée — à utiliser telle quelle
# ============================================================


class NotificationError(Exception):
    """Levée quand l'envoi d'une notification échoue."""

    pass


# ------------------------------------------------------------
# TODO 1 — Créer une notification
# ------------------------------------------------------------
# Entrée  : recipient="alice@example.com", subject="Bienvenue", body="Bonjour Alice"
# Sortie  : Notification(recipient="alice@example.com", subject="Bienvenue", body="Bonjour Alice")
# ------------------------------------------------------------
def create_notification(recipient: str, subject: str, body: str) -> Notification:
    return Notification(recipient, subject, body)


# ------------------------------------------------------------
# TODO 2 — Envoyer une notification via l'API externe
# ------------------------------------------------------------
# Appelle POST https://api.notify.example.com/send avec le JSON :
#   {"to": notification.recipient, "subject": notification.subject, "body": notification.body}
# Retourne True si le statut HTTP est 200.
# Retourne False si le statut HTTP est autre chose.
# ------------------------------------------------------------
def send_notification(notification: Notification) -> bool:
    create = requests.post(
        "https://api.notify.example.com/send",
        json={
            "to": notification.recipient,
            "subject": notification.subject,
            "body": notification.body,
        },
    )
    return create.status_code == 200


# ------------------------------------------------------------
# TODO 3 — Envoyer avec vérification d'erreur réseau
# ------------------------------------------------------------
# Même chose que send_notification, mais :
# Si requests.post lève une requests.ConnectionError,
# lève NotificationError("Service de notification indisponible.")
# Sinon, retourne True si statut 200, False sinon.
# ------------------------------------------------------------
def send_notification_safe(notification: Notification) -> bool:
    try:
        create = requests.post(
            "https://api.notify.example.com/send",
            json={
                "to": notification.recipient,
                "subject": notification.subject,
                "body": notification.body,
            },
        )
        return create.status_code == 200
    except requests.ConnectionError:
        raise NotificationError("Service de notification indisponible.")


# ------------------------------------------------------------
# TODO 4 — Envoyer plusieurs notifications
# ------------------------------------------------------------
# Entrée  : liste de Notification
# Sortie  : nombre d'envois réussis (ceux pour lesquels send_notification retourne True)
# Utilise send_notification — ne recopie pas sa logique
# ------------------------------------------------------------
def send_all(notifications: list[Notification]) -> int:
    compteur = 0
    for i in notifications:
        if send_notification(i):
            compteur += 1
    return compteur


# ------------------------------------------------------------
# TODO 5 — Vérifier qu'un destinataire est valide
# ------------------------------------------------------------
# Entrée  : "alice@example.com"  → True
# Entrée  : "pas-un-email"       → False
# Entrée  : ""                   → False
# Règle : doit contenir exactement un "@" et au moins un "." après le "@"
# ------------------------------------------------------------
def is_valid_recipient(recipient: str) -> bool:
    parts = recipient.split("@")
    if len(parts) != 2:
        return False
    domain = parts[1]
    if "." in domain:
        return True
    else:
        return False
