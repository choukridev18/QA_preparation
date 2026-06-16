# Lance : pytest test_exercise.py -v

import pytest
from exercise import (
    Subscription,
    PricingError,
    UnknownPlanError,
    InvalidDurationError,
    InvalidPromoError,
    base_price,
    discount_rate,
    final_price,
    summary,
)


# ── base_price ────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("plan,months,expected", [
    ("starter", 1,  9.99),
    ("pro",     3, 89.97),
    ("enterprise", 2, 199.98),
])
def test_base_price_valid_plans(plan, months, expected):
    sub = Subscription(plan=plan, months=months)
    assert base_price(sub) == pytest.approx(expected), "Le prix de base est incorrect"


def test_base_price_unknown_plan_raises():
    sub = Subscription(plan="ultra", months=1)
    with pytest.raises(UnknownPlanError, match="ultra"):
        base_price(sub)


def test_base_price_unknown_plan_is_pricing_error():
    sub = Subscription(plan="ultra", months=1)
    with pytest.raises(PricingError):
        base_price(sub)


def test_base_price_zero_months_raises():
    sub = Subscription(plan="pro", months=0)
    with pytest.raises(InvalidDurationError):
        base_price(sub)


def test_base_price_negative_months_raises():
    sub = Subscription(plan="pro", months=-3)
    with pytest.raises(InvalidDurationError):
        base_price(sub)


# ── discount_rate ─────────────────────────────────────────────────────────────

@pytest.mark.parametrize("code,expected", [
    ("WELCOME10", 0.10),
    ("SUMMER20",  0.20),
    ("VIP50",     0.50),
    (None,        0.0),
])
def test_discount_rate_valid_codes(code, expected):
    assert discount_rate(code) == pytest.approx(expected), "Le taux de remise est incorrect"


def test_discount_rate_invalid_code_raises():
    with pytest.raises(InvalidPromoError, match="FAKE99"):
        discount_rate("FAKE99")


# ── final_price ───────────────────────────────────────────────────────────────

def test_final_price_no_promo():
    sub = Subscription(plan="starter", months=2)
    assert final_price(sub) == pytest.approx(19.98), "Sans promo le prix final doit être égal au prix de base"


def test_final_price_with_promo():
    sub = Subscription(plan="pro", months=3, promo_code="WELCOME10")
    assert final_price(sub) == pytest.approx(80.973), "Le prix final avec promo est incorrect"


# ── summary ───────────────────────────────────────────────────────────────────

def test_summary_no_promo():
    sub = Subscription(plan="starter", months=1)
    assert summary(sub) == "starter — 1 mois — 9.99€", "Le résumé sans promo est incorrect"


def test_summary_with_promo():
    sub = Subscription(plan="pro", months=6, promo_code="SUMMER20")
    assert summary(sub) == "pro — 6 mois — 143.95€", "Le résumé avec promo est incorrect"
