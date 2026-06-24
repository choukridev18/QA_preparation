"""
Module de calcul de frais de livraison.

Les frais dépendent du poids (kg) et de la zone géographique.
Des remises s'appliquent aux commandes multiples.
"""

ZONE_RATES: dict[str, float] = {
    "local": 2.50,
    "national": 5.00,
    "international": 12.00,
}

BASE_FEE: float = 1.50


class DeliveryError(ValueError):
    """Levée quand les paramètres de livraison sont invalides."""
    pass


def calculate_shipping(weight: float, zone: str) -> float:
    """
    Calcule les frais de livraison selon le poids et la zone.

    Formule : BASE_FEE + (poids × taux_zone)
    Ex : calculate_shipping(2.0, "local") → 1.50 + (2.0 × 2.50) = 6.50

    Lève DeliveryError si le poids est <= 0 ou si la zone est inconnue.
    """
    if weight <= 0:
        raise DeliveryError(f"Poids invalide : {weight}")
    if zone not in ZONE_RATES:
        raise DeliveryError(f"Zone inconnue : {zone}")
    return BASE_FEE + weight * ZONE_RATES[zone]


def apply_multi_discount(total: float, item_count: int) -> float:
    """
    Applique une remise si la commande contient plusieurs articles.

    - 1 article  : pas de remise
    - 2-4 articles : -10%
    - 5+ articles  : -20%

    Ex : apply_multi_discount(10.0, 3) → 9.0
    """
    if item_count >= 5:
        return total * 0.80
    if item_count >= 2:
        return total * 0.90
    return total


def cheapest_zone(weight: float) -> str:
    """
    Retourne la zone avec les frais les plus bas pour un poids donné.
    Toujours "local" puisque c'est le taux le plus faible.

    Ex : cheapest_zone(5.0) → "local"
    """
    costs = {zone: calculate_shipping(weight, zone) for zone in ZONE_RATES}
    return min(costs, key=lambda z: costs[z])


def is_free_shipping(weight: float, zone: str, item_count: int) -> bool:
    """
    Retourne True si la livraison est gratuite.
    La livraison est gratuite si le total après remise est inférieur à 5.00€.

    Ex : is_free_shipping(0.5, "local", 5) → True  (1.50 + 1.25 = 2.75 × 0.80 = 2.20 < 5.0)
    """
    total = calculate_shipping(weight, zone)
    discounted = apply_multi_discount(total, item_count)
    return discounted < 5.0
