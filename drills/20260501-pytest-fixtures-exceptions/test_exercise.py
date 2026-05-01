# Lance : pytest drills/20260501-pytest-fixtures-exceptions/test_exercise.py -v

import pytest
from exercise import (
    EmptyOrderError,
    InvalidDiscountError,
    Item,
    NegativeQuantityError,
    Order,
    UnknownCustomerError,
    apply_discount,
    calculate_total,
    check_customer_exists,
    validate_not_empty,
    validate_quantities,
)


# --- calculate_total ---

def test_calculate_total_nominal(simple_order):
    assert calculate_total(simple_order) == 12.5, \
        "Total attendu : 1.5*3 + 4.0*2 = 12.5"


def test_calculate_total_empty_order(empty_order):
    assert calculate_total(empty_order) == 0.0, \
        "Une commande vide doit retourner un total de 0.0"


def test_calculate_total_single_item():
    order = Order(customer_id="c1", items=[Item("Crayon", 0.75, 4)])
    assert calculate_total(order) == 3.0, \
        "Total attendu : 0.75 * 4 = 3.0"


# --- validate_not_empty ---

def test_validate_not_empty_raises_on_empty_order(empty_order):
    with pytest.raises(EmptyOrderError):
        validate_not_empty(empty_order)


def test_validate_not_empty_returns_true_on_valid_order(simple_order):
    assert validate_not_empty(simple_order) is True, \
        "Une commande avec des articles doit retourner True"


# --- validate_quantities ---

def test_validate_quantities_raises_on_zero_quantity(order_with_zero_quantity):
    with pytest.raises(NegativeQuantityError):
        validate_quantities(order_with_zero_quantity)


def test_validate_quantities_error_message_contains_item_name(order_with_zero_quantity):
    with pytest.raises(NegativeQuantityError, match="Règle"):
        validate_quantities(order_with_zero_quantity)


def test_validate_quantities_returns_true_when_all_valid(simple_order):
    assert validate_quantities(simple_order) is True, \
        "Toutes les quantités > 0 — doit retourner True"


# --- apply_discount ---

@pytest.mark.parametrize("total,discount,expected", [
    (100.0, 20.0, 80.0),
    (50.0, 0.0, 50.0),
    (200.0, 50.0, 100.0),
    (80.0, 100.0, 0.0),
])
def test_apply_discount_nominal(total, discount, expected):
    assert apply_discount(total, discount) == expected, \
        f"apply_discount({total}, {discount}) devrait retourner {expected}"


def test_apply_discount_raises_on_negative_discount():
    with pytest.raises(InvalidDiscountError):
        apply_discount(100.0, -5.0)


def test_apply_discount_raises_on_discount_above_100():
    with pytest.raises(InvalidDiscountError):
        apply_discount(100.0, 110.0)


# --- check_customer_exists ---

def test_check_customer_exists_returns_true_for_known_id(known_customer_ids):
    assert check_customer_exists("c42", known_customer_ids) is True, \
        "c42 est dans la liste — doit retourner True"


def test_check_customer_exists_raises_for_unknown_id(known_customer_ids):
    with pytest.raises(UnknownCustomerError):
        check_customer_exists("c99", known_customer_ids)


def test_check_customer_exists_error_message_contains_id(known_customer_ids):
    with pytest.raises(UnknownCustomerError, match="c99"):
        check_customer_exists("c99", known_customer_ids)
