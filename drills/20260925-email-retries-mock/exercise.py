# ============================================================
# DRILL — side_effect · return_value · assert_called_with
#         fixtures · pytest.raises · @dataclass
# ============================================================
# Contexte :
#   Module d'envoi d'emails transactionnels pour une app SaaS
#   (confirmation de commande, reset password…). Les mails
#   partent via une API externe (call_mail_api). Les tests
#   mockent cet appel — jamais de vrai réseau.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
#
# À lire dans test_exercise.py :
#   - comment return_value / side_effect sont utilisés
#   - comment assert_called_with vérifie le payload envoyé
# ============================================================

from dataclasses import dataclass


class EmailError(ValueError):
    """Levée quand l'adresse destinataire est invalide."""


class DeliveryError(RuntimeError):
    """Levée quand tous les essais d'envoi ont échoué."""


@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str


def call_mail_api(payload: dict) -> dict:
    """
    Appel HTTP vers l'API mail (fourni — ne pas modifier).
    Les tests mockent cette fonction.
    """
    raise ConnectionError("network unavailable")


# ------------------------------------------------------------
# TODO 1 — validate_recipient
# ------------------------------------------------------------
# Entrée  : "  alice@saas.io  "
# Sortie  : "alice@saas.io"
# Erreur  : EmailError si la chaîne (après strip) ne contient pas "@"
# ------------------------------------------------------------
def validate_recipient(email: str) -> str:
    cleaned = email.strip()
    if "@" not in cleaned:
        raise EmailError("invalid email")
    return cleaned


# ------------------------------------------------------------
# TODO 2 — build_payload
# ------------------------------------------------------------
# Entrée  : EmailMessage(to="a@b.io", subject="Hi", body="Hello")
# Sortie  : {"to": "a@b.io", "subject": "Hi", "body": "Hello", "priority": "normal"}
# ------------------------------------------------------------
def build_payload(message: EmailMessage) -> dict:
    return {
        "to": message.to,
        "subject": message.subject,
        "body": message.body,
        "priority": "normal",
    }


# ------------------------------------------------------------
# TODO 3 — send_email
# ------------------------------------------------------------
# Entrée  : EmailMessage valide
# Comportement :
#   1. validate_recipient(message.to)  → met à jour message.to (ou utilise le résultat)
#   2. build_payload(message)
#   3. call_mail_api(payload) → retourne le dict de réponse tel quel
# ------------------------------------------------------------
def send_email(message: EmailMessage) -> dict:
    message.to = validate_recipient(message.to)
    payload = build_payload(message)
    return call_mail_api(payload)


# ------------------------------------------------------------
# TODO 4 — send_with_retry
# ------------------------------------------------------------
# Entrée  : message, max_attempts=3
# Comportement :
#   Appelle send_email jusqu'à max_attempts fois.
#   Si ConnectionError → réessaie.
#   Si succès → retourne la réponse API.
#   Si tous les essais échouent → lève DeliveryError("max retries exceeded")
# ------------------------------------------------------------
def send_with_retry(message: EmailMessage, max_attempts: int = 3) -> dict:
    for _ in range(max_attempts):
        try:
            return send_email(message)
        except ConnectionError:
            pass
    raise DeliveryError("max retries exceeded")


# ------------------------------------------------------------
# TODO 5 — notify_user
# ------------------------------------------------------------
# Entrée  : to="bob@saas.io", subject="Bienvenue", body="..."
# Sortie  : "sent:{id}"  où id vient de la réponse API (ex: {"id": "msg-9", "status": "ok"})
#           → "sent:msg-9"
# Utilise send_with_retry en interne.
# ------------------------------------------------------------
def notify_user(to: str, subject: str, body: str) -> str:
    message = EmailMessage(to=to, subject=subject, body=body)
    response = send_with_retry(message)
    return f"sent:{response['id']}"


# ------------------------------------------------------------
# TODO 6 — count_failed_attempts
# ------------------------------------------------------------
# Entrée  : liste de résultats booléens [True, False, True, False, False]
# Sortie  : 3  (nombre de False)
# ------------------------------------------------------------
def count_failed_attempts(results: list[bool]) -> int:
    return results.count(False)
