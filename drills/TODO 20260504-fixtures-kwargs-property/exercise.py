# ============================================================
# DRILL — @property · dict unpacking (**) · @pytest.fixture · assert · pytest.raises
# ============================================================
# Contexte :
#   Système de gestion de commandes SaaS.
#   Chaque commande a des articles, une remise et des options
#   de livraison. On fusionne des configs par défaut avec des
#   configs personnalisées grâce à **.
#
# Objectif :
#   Implémenter les fonctions et méthodes ci-dessous pour que
#   tous les tests passent.
#   Lance : pytest drills/20260504-fixtures-kwargs-property/test_exercise.py -v
# ============================================================

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    unit_price: float
    quantity: int


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    discount: float = 0.0        # entre 0.0 et 1.0 (ex: 0.1 = 10 %)
    options: dict = field(default_factory=dict)


# ------------------------------------------------------------
# TODO 1 — @property : total brut
# ------------------------------------------------------------
#
#          la somme de (item.unit_price * item.quantity).
#          Tu dois modifier la classe Order ci-dessus.
# ------------------------------------------------------------
# → Ajoute la @property directement dans la classe Order (ci-dessus).


# ------------------------------------------------------------
# TODO 2 — @property : total après remise
# ------------------------------------------------------------
#
#          le discount sur subtotal.
# ------------------------------------------------------------
# → Ajoute la @property directement dans la classe Order (ci-dessus).


# ------------------------------------------------------------
# TODO 3 — dict unpacking : fusion de configs
# ------------------------------------------------------------
#
# La fonction fusionne les deux dicts passés en arguments AVEC
# un dict par défaut : {"tax": 0.2, "currency": "EUR", "shipping": "standard"}
# Les clés du deuxième argument écrasent celles du premier,
# qui écrasent celles des défauts.
#
# ------------------------------------------------------------
DEFAULT_OPTIONS: dict = {"tax": 0.2, "currency": "EUR", "shipping": "standard"}


def merge_options(base: dict, overrides: dict) -> dict:
    raise NotImplementedError


# ------------------------------------------------------------
# TODO 4 — validation + exception personnalisée
# ------------------------------------------------------------
#
#
#
# ------------------------------------------------------------
def validate_order(order: Order) -> bool:
    raise NotImplementedError


# ------------------------------------------------------------
# TODO 5 — applique les options à une commande
# ------------------------------------------------------------
#           merge_options(order.options, {"shipping": "express"})
#
#          puis retourne l'order.
# ------------------------------------------------------------
def apply_options(order: Order, overrides: dict) -> Order:
    raise NotImplementedError
