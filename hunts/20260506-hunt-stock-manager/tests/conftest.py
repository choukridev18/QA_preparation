import pytest
from src.stock import Product


@pytest.fixture
def sample_products():
    return [
        Product("Clavier", 10.1, 12),
        Product("Souris", 29.99, 3),
        Product("Écran", 299.99, 1),
        Product("Casque", 79.99, 8),
    ]
