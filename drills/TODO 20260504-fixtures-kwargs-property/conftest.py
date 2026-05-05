import pytest
from exercise import Item, Order


@pytest.fixture
def single_item_order():
    """Commande avec un seul article, sans remise."""
    return Order(items=[Item("Stylo", 2.0, 3)])


@pytest.fixture
def multi_item_order():
    """Commande avec plusieurs articles et une remise de 10 %."""
    return Order(
        items=[
            Item("Stylo", 2.0, 3),
            Item("Cahier", 5.0, 1),
            Item("Règle", 1.5, 2),
        ],
        discount=0.1,
    )


@pytest.fixture
def empty_order():
    """Commande vide, sans articles."""
    return Order()
