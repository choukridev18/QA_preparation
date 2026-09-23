from unittest.mock import patch

import pytest

from src.coupons import Coupon, apply_coupon, apply_remote_percent


def test_percent_simple():
    """10% sur 100€ → 90€."""
    coupon = Coupon(code="P10", kind="percent", value=10)
    assert apply_coupon(100, coupon) == 90.0


def test_fixed_simple(save5):
    """5€ de réduction sur 40€ → 35€."""
    assert apply_coupon(40, save5) == 35.0


def test_unknown_kind_raises():
    """Kind inconnu → TypeError."""
    coupon = Coupon(code="X", kind="bogus", value=1)
    with pytest.raises(TypeError):
        apply_coupon(50, coupon)


def test_percent_fractional_result():
    """10% sur 19.99 → 17.99 (attention au float)."""
    coupon = Coupon(code="P10", kind="percent", value=10)
    result = apply_coupon(19.99, coupon)
    assert result == 17.99


def test_welcome10_applies(welcome10):
    """Fixture WELCOME10 : -10% sur 100€ → 90€."""
    assert apply_coupon(100, welcome10) == 90.0


def test_negative_price_raises():
    """Prix négatif → ValueError."""
    coupon = Coupon(code="P10", kind="percent", value=10)
    with pytest.raises(ValueError):
        apply_coupon(-10, coupon)


def test_remote_percent_uses_api_rate():
    """Taux distant mocké à 20% → 80€ sur 100€."""
    with patch("src.coupons.fetch_rate_from_api", return_value=20):
        assert apply_remote_percent(100, "REMOTE20") == 80.0


def test_remote_percent_retries_on_failure():
    """Premier appel API échoue, second réussit."""
    with patch(
        "src.coupons.fetch_rate_from_api",
        side_effect=[RuntimeError("timeout"), 10],
    ):
        with pytest.raises(RuntimeError):
            apply_remote_percent(100, "RETRY10")
        assert apply_remote_percent(100, "RETRY10") == 90.0
