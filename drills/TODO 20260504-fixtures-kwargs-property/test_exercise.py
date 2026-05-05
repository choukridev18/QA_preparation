# Lance : pytest drills/20260504-fixtures-kwargs-property/test_exercise.py -v

import pytest
from exercise import DEFAULT_OPTIONS, Item, Order, apply_options, merge_options, validate_order


# ── TODO 1 & 2 : @property subtotal / total ──────────────────────────────────

def test_subtotal_single_item(single_item_order):
    assert single_item_order.subtotal == 6.0, "subtotal doit être prix × quantité"


def test_subtotal_multi_item(multi_item_order):
    # 2*3 + 5*1 + 1.5*2 = 6 + 5 + 3 = 14
    assert multi_item_order.subtotal == 14.0, "subtotal doit sommer tous les articles"


def test_total_no_discount(single_item_order):
    assert single_item_order.total == 6.0, "sans remise, total == subtotal"


def test_total_with_discount(multi_item_order):
    # 14.0 * 0.9 = 12.6
    assert round(multi_item_order.total, 10) == pytest.approx(12.6), \
        "total doit appliquer la remise sur subtotal"


def test_subtotal_empty_order(empty_order):
    assert empty_order.subtotal == 0.0, "subtotal d'une commande vide doit être 0"


# ── TODO 3 : merge_options (**) ───────────────────────────────────────────────

def test_merge_options_keeps_defaults():
    result = merge_options({}, {})
    assert result == DEFAULT_OPTIONS, "sans surcharge, on doit obtenir les défauts"


def test_merge_options_base_overrides_default():
    result = merge_options({"currency": "USD"}, {})
    assert result["currency"] == "USD", "base doit écraser les défauts"


def test_merge_options_override_wins_over_base():
    result = merge_options({"shipping": "standard"}, {"shipping": "express"})
    assert result["shipping"] == "express", "overrides doit gagner sur base"


def test_merge_options_tax_preserved():
    result = merge_options({"currency": "GBP"}, {"shipping": "express"})
    assert result["tax"] == pytest.approx(0.2), "tax des défauts doit être préservé"


# ── TODO 4 : validate_order ───────────────────────────────────────────────────

def test_validate_empty_order_raises(empty_order):
    with pytest.raises(ValueError, match="aucun article"):
        validate_order(empty_order)


def test_validate_discount_too_high_raises():
    order = Order(items=[Item("X", 1.0, 1)], discount=1.5)
    with pytest.raises(ValueError, match="remise"):
        validate_order(order)


def test_validate_valid_order_returns_true(single_item_order):
    assert validate_order(single_item_order) is True, \
        "une commande valide doit retourner True"


# ── TODO 5 : apply_options ────────────────────────────────────────────────────

def test_apply_options_sets_shipping(single_item_order):
    result = apply_options(single_item_order, {"shipping": "express"})
    assert result.options["shipping"] == "express", \
        "apply_options doit mettre à jour shipping"


def test_apply_options_returns_order(single_item_order):
    result = apply_options(single_item_order, {})
    assert isinstance(result, Order), "apply_options doit retourner un Order"
