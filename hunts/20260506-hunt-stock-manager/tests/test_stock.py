import pytest
from src.stock import (
    Product,
    calculate_stock_value,
    get_low_stock_products,
    apply_discount,
    get_most_expensive,
    total_units,
)


def test_total_units(sample_products):
    """Le nombre total d'unités est la somme des quantités de tous les produits."""
    assert total_units(sample_products) == 24


def test_apply_discount_valid():
    """Une remise de 20% sur 200.0 doit donner 160.0."""
    assert apply_discount(200.0, 20) == 160.0


def test_get_most_expensive(sample_products):
    """Le produit le plus cher doit être l'Écran (299.99)."""
    assert get_most_expensive(sample_products).name == "Écran"


def test_low_stock_count(sample_products):
    """Avec un seuil de 5, exactement 2 produits sont en rupture imminente."""
    low = get_low_stock_products(sample_products, threshold=5)
    assert len(low) == 2


def test_calculate_stock_value():
    """La valeur totale d'un stock avec prix décimaux doit être correcte."""
    products = [Product("Stylo", 0.1, 1), Product("Cahier", 0.2, 1)]
    assert calculate_stock_value(products) == pytest.approx(0.3)


def test_low_stock_names(sample_products):
    """Les produits en rupture imminente (seuil=5) doivent être Écran puis Souris."""
    low = get_low_stock_products(sample_products, threshold=5)
    assert [p.name for p in low] == ["Souris","Écran", ]


def test_apply_discount_invalid_raises():
    """Une remise négative doit lever une exception."""
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)
