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
# Entrée  : Order(customer_id="c1", items=[Item("Stylo", 1.5, 3), Item("Cahier", 4.0, 2)])
# Sortie  : 12.5  (1.5*3 + 4.0*2)
#
# Indice : sum() avec une expression génératrice sur order.items
# ------------------------------------------------------------------
def calculate_total(order: Order) -> float:
    
    return sum(item.price * item.quantity for item in order.items)


# ------------------------------------------------------------------
# TODO 2 — Valider qu'une commande n'est pas vide
# ------------------------------------------------------------------
# Entrée  : Order(customer_id="c1", items=[])
# Attendu : lève EmptyOrderError
#
# Entrée  : Order(customer_id="c1", items=[Item("Stylo", 1.5, 1)])
# Attendu : retourne True
#
# Indice : vérifier len(order.items) et lever l'exception avec raise
# ------------------------------------------------------------------
def validate_not_empty(order: Order) -> bool:
    if len(order.items) == 0:
        raise EmptyOrderError("une commande ne peut pas etre vide")
    return True

   



# ------------------------------------------------------------------
# TODO 3 — Valider les quantités de tous les articles
# ------------------------------------------------------------------
# Entrée  : Order avec Item("Stylo", 1.5, 0)
# Attendu : lève NegativeQuantityError avec le nom de l'article dans le message
#
# Entrée  : Order avec toutes les quantités > 0
# Attendu : retourne True
#
# Indice : boucle sur order.items, raise NegativeQuantityError(f"...{item.name}...")
# ------------------------------------------------------------------
def validate_quantities(order: Order) -> bool:
    for article in order.items:
        if article.quantity == 0:
            raise NegativeQuantityError(f"Quantité invalide pour : {article.name}")
    return True



# ------------------------------------------------------------------
# TODO 4 — Appliquer une remise sur le total
# ------------------------------------------------------------------
# Entrée  : total=100.0, discount=20  → Sortie : 80.0
# Entrée  : total=50.0, discount=0   → Sortie : 50.0
# Entrée  : total=50.0, discount=110 → lève InvalidDiscountError
# Entrée  : total=50.0, discount=-5  → lève InvalidDiscountError
#
# Indice : valider d'abord la plage [0, 100], puis calculer total * (1 - discount/100)
# ------------------------------------------------------------------
def apply_discount(total: float, discount: float) -> float:
    if discount <0 or discount > 100:
        raise InvalidDiscountError("La remise doit être entre 0 et 100")
    return total * (1 - discount /100)


# ------------------------------------------------------------------
# TODO 5 — Vérifier qu'un client existe
# ------------------------------------------------------------------
# Entrée  : customer_id="c42", known_ids=["c1", "c2", "c42"]
# Attendu : retourne True
#
# Entrée  : customer_id="c99", known_ids=["c1", "c2"]
# Attendu : lève UnknownCustomerError avec l'ID dans le message
#
# Indice : opérateur `in` sur une liste, raise avec f-string
# ------------------------------------------------------------------
def check_customer_exists(customer_id: str, known_ids: list[str]) -> bool:
    if not customer_id in known_ids:
        raise UnknownCustomerError(f"le client{customer_id} n'existe pas")
    return True

        
