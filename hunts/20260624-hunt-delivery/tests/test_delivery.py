import pytest
from src.delivery import (
    calculate_shipping,
    apply_multi_discount,
    cheapest_zone,
    is_free_shipping,
    DeliveryError,
)


# ── Tests qui passent ──────────────────────────────────────────────────────────


def test_calculate_shipping_local(local_shipping):
    assert local_shipping == pytest.approx(6.50)


def test_cheapest_zone_is_always_local():
    assert cheapest_zone(5.0) == "local"


def test_delivery_error_on_unknown_zone():
    with pytest.raises(DeliveryError):
        calculate_shipping(1.0, "mars")


# ── Tests avec bugs ────────────────────────────────────────────────────────────


def test_calculate_shipping_international():
    result = calculate_shipping(3.0, "international")
    assert result == 37.5


def test_apply_multi_discount_two_items():
    result = apply_multi_discount(10.0, 2)
    assert result == 9.0


def test_apply_multi_discount_five_items():
    result = apply_multi_discount(50.0, 5)
    assert result == 40.0


def test_delivery_error_on_zero_weight():
    with pytest.raises(DeliveryError):
        calculate_shipping(0, "local")


def test_is_free_shipping_heavy_national(heavy_order):
    result = is_free_shipping(
        heavy_order["weight"],
        heavy_order["zone"],
        heavy_order["items"],
    )
    assert result is False


def test_cheapest_zone_for_light_package():
    result = cheapest_zone(0.1)
    assert result == "local"
