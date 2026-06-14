import pytest


@pytest.fixture
def simple_lines():
    """Deux lignes de facture simples."""
    return [
        {"quantity": 2, "unit_price": 50.0},
        {"quantity": 1, "unit_price": 30.0},
    ]


@pytest.fixture
def single_line():
    """Une seule ligne de facture."""
    return [{"quantity": 3, "unit_price": 33.0}]
