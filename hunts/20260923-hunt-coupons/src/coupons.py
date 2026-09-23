"""Coupon engine — apply percent / fixed discounts to a cart total."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Coupon:
    code: str
    kind: str  # "percent" | "fixed"
    value: float
    max_discount: float | None = None


def apply_coupon(price: float, coupon: Coupon) -> float:
    """
    Apply a coupon to a price and return the discounted amount (2 decimals).

    Raises:
        ValueError: if price is negative
        TypeError: if coupon.kind is unknown
    """
    if price < 0:
        raise ValueError("price must be >= 0")

    if coupon.kind == "percent":
        discount = price * (coupon.value / 100.0)
        if coupon.max_discount is not None:
            discount = min(discount, coupon.max_discount)
        return round(price - discount, 2)

    if coupon.kind == "fixed":
        return round(max(0.0, price - coupon.value), 2)

    raise TypeError(f"unknown coupon kind: {coupon.kind}")


def fetch_rate_from_api(code: str) -> float:
    """
    Pretend to call an external promo API.
    Tests must mock this function — it is not implemented for real.
    """
    raise RuntimeError(f"network call not available for code={code}")


def apply_remote_percent(price: float, code: str) -> float:
    """Fetch a percent rate remotely, then apply it to price."""
    rate = fetch_rate_from_api(code)
    return round(price * (1 - rate / 100.0), 2)
