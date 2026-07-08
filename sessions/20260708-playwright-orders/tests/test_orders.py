import pytest
from playwright.sync_api import Page, expect
from pages.orders_page import OrdersPage


def test_all_orders_displayed(page: Page):
    """Sans filtre, les 5 commandes sont affichées"""
    p = OrdersPage(page)
    p.navigate()

    assert p.get_order_count() == 5


def test_filter_by_pending(page: Page):
    """Filtrer par 'en attente' → 2 commandes"""
    p = OrdersPage(page)
    p.navigate()
    p.filter_by_status("en attente")

    assert p.get_order_count() == 2


def test_change_status_updates_display(page: Page):
    """Changer le statut de la commande 1 → le statut affiché change"""
    p = OrdersPage(page)
    p.navigate()
    p.change_order_status(1, "livrée")

    assert p.get_order_status(1) == "livrée"


def test_shows_number_order_filter_by_deliver(page: Page):
    """Verifier le nombre de commandes affichées"""
    p = OrdersPage(page)
    p.navigate()
    p.filter_by_status("livrée")
    assert p.get_order_count() == 2


def test_pending_count_is_two(page: Page):
    """Au chargement, le compteur en attente vaut 2"""
    p = OrdersPage(page)
    p.navigate()
    assert p.get_pending_count() == 2
