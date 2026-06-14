# Lance : pytest test_exercise.py -v

import pytest
from exercise import Order, Item, OrderError, create_order, ORDER_COUNT
import exercise


# --- TODO 1 : empty_order ---

def test_empty_order_is_pending(empty_order):
    """La commande vide a le statut 'pending'."""
    assert empty_order.status == "pending", "Le statut initial doit être 'pending'"


def test_empty_order_has_no_items(empty_order):
    """La commande vide n'a pas d'articles."""
    assert empty_order.items == [], "La liste d'articles doit être vide"


def test_empty_order_total_is_zero(empty_order):
    """Le total d'une commande vide est 0."""
    assert empty_order.total() == 0.0, "Le total d'une commande vide doit être 0"


# --- TODO 2 : order_with_items ---

def test_order_with_items_has_two_items(order_with_items):
    """La commande avec articles contient exactement 2 articles."""
    assert len(order_with_items.items) == 2, "La commande doit avoir 2 articles"


def test_order_with_items_total(order_with_items):
    """Le total de la commande est 49.99 + 2×29.99 = 109.97."""
    assert pytest.approx(order_with_items.total()) == 109.97, "Total incorrect"


def test_order_with_items_can_be_confirmed(order_with_items):
    """Une commande avec articles peut être confirmée."""
    order_with_items.confirm()
    assert order_with_items.status == "confirmed"


def test_empty_order_isolation(empty_order):
    """Chaque test reçoit une nouvelle commande vide (isolation fixture function)."""
    empty_order.add_item(Item("Test", 1.0, 1))
    assert len(empty_order.items) == 1


def test_empty_order_still_empty_in_next_test(empty_order):
    """La fixture function recrée une commande vide à chaque test."""
    assert len(empty_order.items) == 0, "La fixture doit être réinitialisée entre les tests"


# --- TODO 3 : order_counter avec yield ---

def test_order_counter_starts_at_zero(order_counter):
    """Le compteur démarre à 0 au début du test."""
    assert order_counter == 0, "Le compteur doit valoir 0 en début de test"


def test_create_order_increments_counter(order_counter):
    """create_order incrémente le compteur global."""
    create_order(1)
    create_order(2)
    assert exercise.ORDER_COUNT == 2, "Le compteur doit valoir 2 après 2 créations"


# --- TODO 4 : log_test_name autouse ---

def test_autouse_fixture_runs_automatically(capsys):
    """La fixture autouse s'exécute sans être injectée explicitement."""
    print("message du test")
    captured = capsys.readouterr()
    assert "message du test" in captured.out, "Le print du test doit apparaître"
