import pytest

from src.pipeline import Order


@pytest.fixture
def sample_orders():
    orders = [
        Order(id="o1", category="Livres", amount=30.0, status="valid"),
        Order(id="o2", category="Jeux", amount=60.0, status="invalid"),
        Order(id="o3", category="Livres", amount=20.0, status="valid"),
        Order(id="o4", category="Jeux", amount=45.0, status="valid"),
    ]
    return orders
