import pytest
from src.delivery import calculate_shipping


@pytest.fixture
def local_shipping():
    return calculate_shipping(2.0, "local")


@pytest.fixture
def heavy_order():
    return {"weight": 10.0, "zone": "national", "items": 5}


@pytest.fixture
def multi_items():
    items = [1.0, 2.5, 0.8, 3.2]
    return items
