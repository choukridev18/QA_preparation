# ============================================================
# DRILL — pytest.fixture · pytest.raises · exceptions personnalisées · conftest · type hints
# ============================================================
# Contexte :
#   Tu travailles sur le backend d'une app e-commerce.
#   Le module de commandes valide chaque commande avant de l'enregistrer.
#   Toute règle métier violée lève une exception précise — jamais un retour None.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest drills/20260501-pytest-fixtures-exceptions/test_exercise.py -v
# ============================================================

from dataclasses import dataclass, field
from logging import raiseExceptions


# ------------------------------------------------------------------
# Exceptions métier — déjà définies, ne pas modifier
# ------------------------------------------------------------------

class EmptyOrderError(Exception):

    """Commande sans aucun article."""
    

class NegativeQuantityError(Exception):
    """Quantité d'un article inférieure ou égale à zéro."""


class InvalidDiscountError(Exception):
    """Remise hors de la plage autorisée [0, 100]."""


class UnknownCustomerError(Exception):
    """Client introuvable dans la base."""


# ------------------------------------------------------------------
# Modèle de données — déjà défini, ne pas modifier
# ------------------------------------------------------------------

@dataclass
class Item:
    name: str
    price: float
    quantity: int


@dataclass
class Order:
    customer_id: str
    items: list[Item] = field(default_factory=list)


# ------------------------------------------------------------------
# TODO 1 — Calculer le total d'une commande
# ------------------------------------------------------------------
#
# ------------------------------------------------------------------
def calculate_total(order: Order) -> float:
    
    return sum(item.price * item.quantity for item in order.items)


# ------------------------------------------------------------------
# TODO 2 — Valider qu'une commande n'est pas vide
# ------------------------------------------------------------------
#
#
# ------------------------------------------------------------------
def validate_not_empty(order: Order) -> bool:
    if len(order.items) == 0:
        raise EmptyOrderError("une commande ne peut pas etre vide")
    return True

   



# ------------------------------------------------------------------
# TODO 3 — Valider les quantités de tous les articles
# ------------------------------------------------------------------
#
#
# ------------------------------------------------------------------
def validate_quantities(order: Order) -> bool:
    for article in order.items:
        if article.quantity == 0:
            raise NegativeQuantityError(f"Quantité invalide pour : {article.name}")
    return True



# ------------------------------------------------------------------
# TODO 4 — Appliquer une remise sur le total
# ------------------------------------------------------------------
#
# ------------------------------------------------------------------
def apply_discount(total: float, discount: float) -> float:
    if discount <0 or discount > 100:
        raise InvalidDiscountError("La remise doit être entre 0 et 100")
    return total * (1 - discount /100)


# ------------------------------------------------------------------
# TODO 5 — Vérifier qu'un client existe
# ------------------------------------------------------------------
#
#
# ------------------------------------------------------------------
def check_customer_exists(customer_id: str, known_ids: list[str]) -> bool:
    if not customer_id in known_ids:
        raise UnknownCustomerError(f"le client{customer_id} n'existe pas")
    return True

        
