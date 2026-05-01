import pytest
from exercise import Item, Order


@pytest.fixture
def empty_order():
    return Order(customer_id="c1", items=[])


@pytest.fixture
def simple_order():
    return Order(
        customer_id="c1",
        items=[
            Item(name="Stylo", price=1.5, quantity=3),
            Item(name="Cahier", price=4.0, quantity=2),
        ],
    )


@pytest.fixture
def order_with_zero_quantity():
    return Order(
        customer_id="c2",
        items=[
            Item(name="Gomme", price=0.5, quantity=1),
            Item(name="Règle", price=2.0, quantity=0),
        ],
    )


@pytest.fixture
def known_customer_ids():
    return ["c1", "c2", "c42", "c100"]
