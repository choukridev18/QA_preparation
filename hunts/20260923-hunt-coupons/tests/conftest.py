import pytest

from src.coupons import Coupon


@pytest.fixture
def welcome10():
    """Coupon WELCOME10 : -10% sans plafond."""
    return Coupon(code="WELCOME10", kind="percent", value=10)


@pytest.fixture
def save5():
    """Coupon SAVE5 : -5€ fixe."""
    return Coupon(code="SAVE5", kind="fixed", value=5)
