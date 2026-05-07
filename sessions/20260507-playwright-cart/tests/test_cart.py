
import pytest
from playwright.sync_api import Page, expect

from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage


def test_add_item_to_cart(page: Page, app_url: str):
    """Ajouter un article depuis le catalogue et vérifier qu'il apparaît dans le panier"""
    catalog = CatalogPage(page)
    catalog.navigate()
    catalog.add_to_cart("Clavier mécanique")
    catalog.go_to_cart()
    cart = CartPage(page)
    expect(page).to_have_url(f"{app_url}/cart")
    assert cart.get_item_count() == 1


def test_update_quantity_recalculates_total(page: Page, app_url: str):
    """Modifier la quantité d'un article met à jour le total"""
    catalog = CatalogPage(page)
    catalog.navigate()
    catalog.add_to_cart("Souris ergonomique")
    catalog.go_to_cart()
    cart = CartPage(page)
    cart.update_quantity("Souris ergonomique", 3)
    expect(page).to_have_url(f"{app_url}/cart")
    assert cart.get_total() == pytest.approx(136.50, rel=0.01)


def test_remove_item_shows_empty_cart(page: Page, app_url: str):
    """Supprimer le seul article du panier affiche le message panier vide"""
    catalog = CatalogPage(page)
    catalog.navigate()
    catalog.add_to_cart("Casque audio")
    catalog.go_to_cart()
    cart = CartPage(page)
    cart.remove_item("Casque audio")
    assert cart.get_item_count() == 0
    expect(page.locator("#empty-message")).to_be_visible()

def test_add_two_items_shows_count_of_two(page: Page,app_url:str):
    """Ajouter deux articles différents affiche 2 lignes dans le panier"""
    catalog = CatalogPage(page)
    catalog.navigate()
    catalog.add_to_cart("Souris ergonomique")
    catalog.add_to_cart("Casque audio")
    catalog.go_to_cart()
    cart = CartPage(page)
    assert cart.get_item_count() ==2


def test_continue_shopping_link_returns_to_catalog(page: Page, app_url: str):
    """Cliquer sur 'Continuer mes achats' depuis le panier ramène au catalogue"""
    cart = CartPage(page)
    cart.navigate()
    page.get_by_role("link", name="Continuer mes achats").click()
    expect(page).to_have_url(f"{app_url}/")

