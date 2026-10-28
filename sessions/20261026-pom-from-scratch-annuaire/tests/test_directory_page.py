from playwright.sync_api import expect
from pages.directory_page import DirectoryPage
import pytest


def test_without_search_list_shows_every_workers(directory: DirectoryPage):
    """Sans recherche, la liste affiche tous les collègues."""

    assert len(directory.get_result_names()) == 5


def test_only_result(directory: DirectoryPage):
    """Une recherche qui matche un nom affiche ce collègue."""
    directory.search("Karim")
    assert "Karim Benali" in directory.get_result_names()


def test_only_shows_search_result(directory: DirectoryPage):
    """Une recherche ne montre pas les collègues qui ne correspondent pas."""
    directory.search("Karim")
    assert len(directory.get_result_names()) == 1
    assert not directory.is_colleague_displayed("Léa Martin")


def test_without_result_shows_state_empty(directory: DirectoryPage):
    """Une recherche sans résultat affiche le message d'état vide."""
    directory.search("inexistant")
    assert directory.get_empty_message() == "Aucun collègue trouvé."
    expect(directory.page.locator("#empty-message")).to_be_visible()
    assert directory.get_result_count() == 0


def test_search_ignores_letter_case(directory: DirectoryPage):
    """La recherche ne tient pas compte des majuscules / minuscules."""
    directory.search("léa MaRtin")
    assert "Léa Martin" in directory.get_result_names()
