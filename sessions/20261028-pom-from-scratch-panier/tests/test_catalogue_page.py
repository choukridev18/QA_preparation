from re import A
from playwright.sync_api import expect
from pages.catalogue import CataloguePage


def test_catalogue_shows_3_products(catalogue: CataloguePage):
    """le catalogue affiche 3 produits proposé"""
    assert catalogue.get_count_products() == 3


def test_added_one_product_shows_1_on_the_basket(catalogue: CataloguePage):
    """ajouter un produit affiche 1 sur le panier"""
    catalogue.add_to_basket("Souris sans fil")
    assert catalogue.get_count_badge() == 1


def test_basket_page_shows_product_added(catalogue: CataloguePage):
    """le produit ajouté s affiche sur la page panier"""
    catalogue.add_to_basket("Souris sans fil")
    catalogue.go_to_cart()
    expect(catalogue.page).to_have_url(f"{catalogue.URL}/cart")
    assert "Souris sans fil" in catalogue.get_list_products_added()


def test_total_prices_matches_products(catalogue: CataloguePage):
    """Le total affiché correspond au prix du produit (une unité)."""
    assert catalogue.get_product_price("Souris sans fil") == "29.50 €"
    catalogue.add_to_basket("Souris sans fil")
    catalogue.go_to_cart()
    assert catalogue.get_total_price() == "Total : 29.50 €"


def test_total_two_products_added(catalogue: CataloguePage):
    """Deux produits différents ajoutés → total = somme des deux prix."""
    produit1 = catalogue.convert_price_product_in_float("Souris sans fil")
    assert produit1 == 29.50
    produit2 = catalogue.convert_price_product_in_float("Clavier compact")
    assert produit2 == 49.90
    total = produit1 + produit2
    catalogue.add_to_basket("Souris sans fil")
    catalogue.add_to_basket("Clavier compact")
    catalogue.go_to_cart()
    assert str(total) in catalogue.get_total_price()
