import requests

CALENDAR_API_URL = "https://api.calendar.example.com"

BOOKINGS: dict = {}
_next_id: int = 1


def get_available_slots(date: str) -> list[dict]:
    """
    Récupère les créneaux disponibles pour une date donnée.

    Appelle GET /slots?date=<date> sur l'API calendrier.
    Retourne la liste des créneaux (dicts avec au moins la clé 'id').
    Lève requests.HTTPError si le serveur répond avec une erreur.
    """
    response = requests.get(f"{CALENDAR_API_URL}/slots", params={"date": date})
    response.raise_for_status()
    return response.json()["slots"]


def send_confirmation_email(user_email: str, booking_id: str) -> bool:
    """
    Envoie un email de confirmation après une réservation.

    Appelle POST /notify avec {email, booking_id}.
    Retourne True si le serveur répond avec le code 200, False sinon.
    """
    response = requests.post(
        f"{CALENDAR_API_URL}/notify",
        json={"email": user_email, "booking_id": booking_id},
    )
    return response.status_code == 200


def book_slot(slot_id: int, user_email: str) -> str:
    """
    Réserve un créneau et retourne l'identifiant de réservation.

    L'identifiant a le format 'BOOKING-XXXX' (4 chiffres, zéro-padded).
    La réservation est stockée en mémoire dans BOOKINGS.
    """
    global _next_id
    booking_id = f"BOOKING-{_next_id:04d}"
    BOOKINGS[booking_id] = {"slot_id": slot_id, "user_email": user_email}
    _next_id += 1
    return booking_id


def cancel_booking(booking_id: str) -> bool:
    """
    Annule une réservation existante.

    Retourne True si l'annulation réussit.
    Lève ValueError si booking_id n'existe pas dans BOOKINGS.
    """
    if booking_id not in BOOKINGS:
        raise ValueError(f"Réservation '{booking_id}' introuvable.")
    del BOOKINGS[booking_id]
    return True


def calculate_price(base_price: float, discount_rate: float) -> float:
    """
    Applique une remise au prix de base.

    discount_rate : flottant entre 0.0 (aucune remise) et 1.0 (gratuit).
    Exemple : calculate_price(100.0, 0.2) → 80.0
    """
    return base_price * (1 - discount_rate)
