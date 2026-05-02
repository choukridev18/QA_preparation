from multiprocessing import Value
import pytest
from unittest.mock import patch

from src.pipeline import (
    Order,
    compute_discount,
    fetch_exchange_rate,
    filter_valid_orders,
    get_category_totals,
    sort_by_amount,
)


# ---------------------------------------------------------------
# Tests corrects — ceux-ci passent déjà
# ---------------------------------------------------------------

def test_filter_valid_orders_removes_invalid():
    orders = [
        Order("o1", "A", 100.0, "valid"),
        Order("o2", "B", 50.0, "invalid"),
        Order("o3", "A", 0.0, "valid"),
    ]
    result = filter_valid_orders(orders)
    assert len(result) == 1
    assert result[0].id == "o1"


def test_compute_discount_promo10():
    result = compute_discount(200.0, "PROMO10")
    assert result == 180.0, "PROMO10 doit retirer 10% → 200 * 0.9 = 180"


def test_get_category_totals_multiple_categories():
    orders = [
        Order("o1", "Livres", 30.0, "valid"),
        Order("o2", "Jeux", 60.0, "valid"),
        Order("o3", "Livres", 20.0, "valid"),
    ]
    result = get_category_totals(orders)
    assert result == {"Livres": 50.0, "Jeux": 60.0}


# ---------------------------------------------------------------
# Tests avec bugs intentionnels — à corriger
# ---------------------------------------------------------------

def test_sort_by_amount_returns_descending():
    orders = [
        Order("o1", "A", 50.0, "valid"),
        Order("o2", "B", 200.0, "valid"),
        Order("o3", "A", 100.0, "valid"),
    ]
    result = sort_by_amount(orders)
    assert [o.amount for o in result] == [200.0, 100.0, 50.0]  # BUG 1


def test_filter_valid_orders_with_fixture(sample_orders):
    result = filter_valid_orders(sample_orders)
    assert len(result) == 3, "3 commandes valides attendues sur 4"  # BUG 2
    

def test_compute_discount_invalid_code_raises():
    with pytest.raises(ValueError):  # BUG 3
        compute_discount(100.0, "INVALIDE")


def test_get_category_totals_empty_list():
    result = get_category_totals([])
    assert result == {} # BUG 4
    


def test_fetch_exchange_rate_mocked():
    with patch("src.pipeline.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rate": 1.08}  # BUG 5
        result = fetch_exchange_rate("USD")
    assert result == 1.08, "Le taux EUR/USD doit être 1.08"
