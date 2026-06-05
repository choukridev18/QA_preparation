# ============================================================
# DRILL — mock.patch · return_value · fixtures · parametrize
# ============================================================
# Contexte :
#   Service de notifications pour une app SaaS.
#   Le service envoie des messages via email ou SMS selon le
#   canal préféré de chaque utilisateur. Les appels aux APIs
#   externes (email, SMS) sont mockés dans les tests.
#
# Objectif :
#   Implémenter les 5 fonctions ci-dessous pour que tous les
#   tests passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

from dataclasses import dataclass
from exercise_services import send_email_api, send_sms_api


@dataclass
class User:
    name: str
    email: str
    phone: str
    channel: str  # "email" ou "sms"


# ------------------------------------------------------------
# TODO 1 — Formater un message
# ------------------------------------------------------------
# Entrée  : template="Bonjour {name}, votre commande est prête.",
#           name="Alice"
# Sortie  : "Bonjour Alice, votre commande est prête."
# ------------------------------------------------------------
def format_message(template: str, name: str) -> str:
    return template.replace("{name}", name)


# ------------------------------------------------------------
# TODO 2 — Envoyer un email
# ------------------------------------------------------------
# Appelle send_email_api(user.email, subject, body)
# Retourne le résultat de cet appel (bool).
# Entrée  : user=User("Alice", "alice@ex.com", ...), subject="Bienvenue",
#           body="Bonjour Alice"
# Sortie  : True si send_email_api retourne True
# ------------------------------------------------------------
def notify_by_email(user: User, subject: str, body: str) -> bool:
    return send_email_api(user.email, subject, body)


# ------------------------------------------------------------
# TODO 3 — Envoyer un SMS
# ------------------------------------------------------------
# Appelle send_sms_api(user.phone, message)
# Retourne le résultat de cet appel (bool).
# Entrée  : user=User(..., phone="+33600000001", ...), message="Bonjour Alice"
# Sortie  : True si send_sms_api retourne True
# ------------------------------------------------------------
def notify_by_sms(user: User, message: str) -> bool:
    return send_sms_api(user.phone, message)


# ------------------------------------------------------------
# TODO 4 — Dispatcher selon le canal
# ------------------------------------------------------------
# Si user.channel == "email" : appelle notify_by_email(user, "Notification", message)
# Si user.channel == "sms"   : appelle notify_by_sms(user, message)
# Retourne True si succès, False sinon.
# ------------------------------------------------------------
def notify_user(user: User, message: str) -> bool:
    if user.channel == "email":
        return notify_by_email(user, "Notification", message)
    elif user.channel == "sms":
        return notify_by_sms(user, message)
    else:
        return False


# ------------------------------------------------------------
# TODO 5 — Compter les succès
# ------------------------------------------------------------
# Reçoit une liste de booléens.
# Retourne le nombre de True dans la liste.
# Entrée  : [True, False, True, True]
# Sortie  : 3
# ------------------------------------------------------------
def count_successful(results: list) -> int:
    return results.count(True)
