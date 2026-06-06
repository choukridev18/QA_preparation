import pytest
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage


def test_dashboard_shows_all_tickets_without_filter(page: Page):
    """Sans filtre, les 6 tickets sont visibles."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    expect(page.locator("#ticket-count")).to_have_text("6 ticket(s) affiché(s)")
    titles = dashboard.get_visible_titles()
    assert len(titles) == 6


def test_filter_by_status_shows_only_matching(page: Page):
    """Filtre statut « ouvert » : seuls les tickets ouverts apparaissent."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    dashboard.set_status_filter("ouvert")
    dashboard.apply_filters()
    expect(page.locator("#ticket-count")).to_have_text("2 ticket(s) affiché(s)")
    titles = dashboard.get_visible_titles()
    assert "Bug connexion impossible" in titles
    assert "Export CSV ne fonctionne pas" in titles
    assert len(titles) == 2


def test_search_with_no_match_shows_empty_state(page: Page):
    """Recherche sans résultat : message d'absence et compteur à zéro."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    dashboard.set_search("zzzzintrouvable")
    dashboard.apply_filters()
    expect(page.locator("#ticket-count")).to_have_text("0 ticket(s) affiché(s)")
    expect(page.locator("#no-results")).to_be_visible()


def test_reset_filters_restores_all_tickets(page: Page):
    """Après filtrage puis reset, tous les tickets réapparaissent."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    dashboard.set_status_filter("ferme")
    dashboard.apply_filters()
    expect(page.locator("#ticket-count")).to_have_text("2 ticket(s) affiché(s)")
    dashboard.reset_filters()
    expect(page.locator("#ticket-count")).to_have_text("6 ticket(s) affiché(s)")


def test_priority_high_alone(page: Page):
    """Affiche que les titres de haute priorité"""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    dashboard.set_status_filter("")
    dashboard.set_priority_filter("haute")
    dashboard.apply_filters()
    expect(page.locator("#ticket-count")).to_have_text("3 ticket(s) affiché(s)")
    titles = dashboard.get_visible_titles()
    assert "Bug connexion impossible" in titles
    assert "Lenteur page tableau de bord" in titles
    assert "Erreur 500 sur facturation" in titles


def test_status_and_priority_with_one_ticket(page: Page):
    """Statut en_cours + priorité haute : seul 'Lenteur page tableau de bord' s'affiche."""
    dashboard = DashboardPage(page)
    dashboard.navigate()
    dashboard.set_status_filter("en_cours")
    dashboard.set_priority_filter("haute")
    dashboard.apply_filters()
    nbr = dashboard.get_displayed_count()
    assert nbr == 1
    title = dashboard.get_visible_titles()
    assert "Lenteur page tableau de bord" in title
