from playwright.sync_api import Page, expect
from pages.catalog_page import CatalogPage


def test_catalog_shows_all_products_by_default(page: Page):
    """Le catalogue affiche 6 produits par défaut."""
    p = CatalogPage(page)
    p.navigate()
    assert p.get_result_count() == 6


def test_search_by_keyword_filters_results(page: Page):
    """Rechercher 'Laptop' affiche uniquement le Laptop Pro."""
    p = CatalogPage(page)
    p.navigate()
    p.fill_search("Laptop")
    p.submit_search()
    assert p.get_result_count() == 1
    assert "Laptop Pro" in p.get_product_names()


def test_filter_by_category_audio(page: Page):
    """Filtrer par 'Audio' affiche 2 produits."""
    p = CatalogPage(page)
    p.navigate()
    p.select_category("Audio")
    p.submit_search()
    assert p.get_result_count() == 2


def test_search_with_no_match_shows_empty_message(page: Page):
    """Rechercher un mot inconnu affiche le message 'Aucun produit'."""
    p = CatalogPage(page)
    p.navigate()
    p.fill_search("zzzinexistant")
    p.submit_search()
    assert p.has_no_results_message() is True


def test_reset_filters_restores_full_catalog(page: Page):
    """Réinitialiser après un filtre recharge tous les produits."""
    p = CatalogPage(page)
    p.navigate()
    p.select_category("Mobilier")
    p.submit_search()
    p.reset_filters()
    assert p.get_result_count() == 6


def test_filter_by_category_mobilier(page: Page):
    """filtrer par Mobiler affiche 2 produits"""
    p = CatalogPage(page)
    p.navigate()
    p.select_category("Mobilier")
    p.submit_search()
    assert p.get_result_count() == 2


def test_search_products_in_category(page: Page):
    """Rechercher 'Casque' dans categorie 'Audio'"""
    p = CatalogPage(page)
    p.navigate()
    p.fill_search("Casque")
    p.select_category("Audio")
    p.submit_search()
    assert "Casque audio" in p.get_product_names()
