"""Pipeline de traitement de commandes — code de production correct."""

from dataclasses import dataclass

import requests


@dataclass
class Order:
    id: str
    category: str
    amount: float
    status: str  # "valid" ou "invalid"


def filter_valid_orders(orders: list[Order]) -> list[Order]:
    """Retourne uniquement les commandes valides (status == 'valid' et amount > 0)."""
    return [o for o in orders if o.status == "valid" and o.amount > 0]


def sort_by_amount(orders: list[Order]) -> list[Order]:
    """Retourne les commandes triées par montant décroissant."""
    return sorted(orders, key=lambda o: o.amount, reverse=True)


def get_category_totals(orders: list[Order]) -> dict[str, float]:
    """Retourne le total des montants par catégorie.

    Exemple :
        [Order("o1", "A", 100.0, "valid"), Order("o2", "A", 50.0, "valid")]
        → {"A": 150.0}
    """
    totals: dict[str, float] = {}
    for order in orders:
        totals[order.category] = totals.get(order.category, 0.0) + order.amount
    return totals


def compute_discount(amount: float, code: str) -> float:
    """Applique un code promo et retourne le montant réduit.

    Codes valides : "PROMO10" (-10%), "PROMO20" (-20%)

    Raises:
        ValueError: si le code est inconnu
    """
    discounts = {"PROMO10": 0.10, "PROMO20": 0.20}
    if code not in discounts:
        raise ValueError(f"Code promo inconnu : {code}")
    return round(amount * (1 - discounts[code]), 2)


def fetch_exchange_rate(currency: str) -> float:
    """Appelle une API externe et retourne le taux de change vers EUR.

    Raises:
        ConnectionError: si l'API répond avec un statut 500
    """
    response = requests.get(f"https://api.rates.example.com/{currency}")
    if response.status_code == 500:
        raise ConnectionError("Erreur serveur API taux de change")
    return response.json()["rate"]
