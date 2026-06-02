import pytest
from src.pricing import (
    apply_discount,
    calculate_tva,
    final_price,
    get_cheapest_items,
    validate_discount,
)


# ------------------------------------------------------------------ #
# Tests corrects — ils passent dès le départ                          #
# ------------------------------------------------------------------ #


def test_apply_discount_half(base_price):
    """50% discount on 100 → 50.0"""
    assert apply_discount(base_price, 0.5) == 50.0


def test_calculate_tva_standard(base_price):
    """TVA 20% on 100 → 120.0"""
    assert calculate_tva(base_price) == 120.0


def test_validate_discount_valid():
    """Valid discount rates (0, 0.5, 1.0) must not raise"""
    validate_discount(0.0)
    validate_discount(0.5)
    validate_discount(1.0)


# ------------------------------------------------------------------ #
# Tests avec bugs — à corriger                                         #
# ------------------------------------------------------------------ #


def test_apply_discount_one_third():
    """1/3 discount on 30 → approximately 20.0"""
    result = apply_discount(30, 1 / 3)
    assert result == pytest.approx(20.0)


def test_validate_discount_above_one():
    """discount_rate > 1 must raise an exception"""
    with pytest.raises(ValueError):
        validate_discount(1.5)


def test_get_cheapest_three(sample_prices):
    """3 cheapest items from [15.0, 3.0, 8.5, 1.0, 22.0] → sorted ascending"""
    result = get_cheapest_items(sample_prices, 3)
    assert result == [1.0, 3.0, 8.5]


def test_final_price_no_discount(base_price):
    """No discount (0%), TVA 20% on 100 → 120.0"""
    result = final_price(base_price, 0, 0.20)
    assert result == pytest.approx(120.0)
