# ============================================================
# DRILL — pytest.fixture · scope · yield · autouse · conftest
# ============================================================
# Contexte :
#   Un système de gestion de commandes SaaS. Les commandes
#   ont un statut (pending, confirmed, cancelled) et une liste
#   d'articles. Le module ci-dessous est correct — tu n'as
#   pas besoin de le modifier.
#
# Objectif :
#   Implémenter les fixtures dans conftest.py pour que tous
#   les tests dans test_exercise.py passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

from dataclasses import dataclass, field


class OrderError(ValueError):
    """Levée quand une opération sur une commande est invalide."""
    pass


@dataclass
class Item:
    name: str
    price: float
    quantity: int


@dataclass
class Order:
    id: int
    status: str = "pending"
    items: list[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        if self.status != "pending":
            raise OrderError(f"Impossible d'ajouter un article à une commande '{self.status}'.")
        self.items.append(item)

    def confirm(self) -> None:
        if not self.items:
            raise OrderError("Impossible de confirmer une commande vide.")
        self.status = "confirmed"

    def cancel(self) -> None:
        if self.status == "cancelled":
            raise OrderError("La commande est déjà annulée.")
        self.status = "cancelled"

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)


# ------------------------------------------------------------
# TODO 1 — Fixture de base : une commande vide
# ------------------------------------------------------------
# À implémenter dans conftest.py
# Nom       : empty_order
# Retourne  : une Order avec id=1, status="pending", items=[]
# Scope     : function (par défaut)
# ------------------------------------------------------------

# ------------------------------------------------------------
# TODO 2 — Fixture avec données : une commande avec 2 articles
# ------------------------------------------------------------
# À implémenter dans conftest.py
# Nom       : order_with_items
# Dépend de : empty_order (utilise la fixture comme paramètre)
# Ajoute    : Item("Clavier", 49.99, 1) et Item("Souris", 29.99, 2)
# Retourne  : la commande avec les 2 articles
# ------------------------------------------------------------

# ------------------------------------------------------------
# TODO 3 — Fixture avec yield : reset du compteur global
# ------------------------------------------------------------
# À implémenter dans conftest.py
# Nom       : order_counter
# Comportement :
#   - Setup   : initialise ORDER_COUNT = 0 dans ce module
#   - yield   : ORDER_COUNT (la valeur initiale)
#   - Teardown: remet ORDER_COUNT à 0
# Scope     : function
# ------------------------------------------------------------

# Compteur global utilisé par la fixture order_counter
ORDER_COUNT: int = 0


def create_order(order_id: int) -> Order:
    """Crée une commande et incrémente le compteur global."""
    global ORDER_COUNT
    ORDER_COUNT += 1
    return Order(id=order_id)


# ------------------------------------------------------------
# TODO 4 — Fixture autouse : log des tests
# ------------------------------------------------------------
# À implémenter dans conftest.py
# Nom       : log_test_name (autouse=True)
# Comportement :
#   - Setup   : affiche "--- début test ---" avec print()
#   - yield
#   - Teardown: affiche "--- fin test ---" avec print()
# Scope     : function
# ------------------------------------------------------------
