import pytest
from exercise import Order, Item, create_order
import exercise


# ------------------------------------------------------------
# TODO 1 — Fixture empty_order
# ------------------------------------------------------------
# Retourne une Order(id=1) vide, scope function
# ------------------------------------------------------------
@pytest.fixture
def empty_order():
    return Order(id=1)


# ------------------------------------------------------------
# TODO 2 — Fixture order_with_items
# ------------------------------------------------------------
# Dépend de empty_order, ajoute 2 articles
# ------------------------------------------------------------
@pytest.fixture
def order_with_items(empty_order):
    empty_order.add_item(Item("Clavier", 49.99, 1))
    empty_order.add_item(Item("Souris", 29.99, 2))
    return empty_order


# ------------------------------------------------------------
# TODO 3 — Fixture order_counter avec yield
# ------------------------------------------------------------
# Setup : exercise.ORDER_COUNT = 0
# yield : exercise.ORDER_COUNT
# Teardown : exercise.ORDER_COUNT = 0
# ------------------------------------------------------------
@pytest.fixture
def order_counter():
    exercise.ORDER_COUNT = 0
    yield exercise.ORDER_COUNT
    exercise.ORDER_COUNT = 0


# ------------------------------------------------------------
# TODO 4 — Fixture log_test_name (autouse=True)
# ------------------------------------------------------------
# print("--- début test ---") / yield / print("--- fin test ---")
# ------------------------------------------------------------


@pytest.fixture(autouse=True)
def log_test_name():
    print("--- début test ---")
    yield
    print("--- fin test ---")
