import pytest
from playwright.sync_api import Page, expect

from pages.todos_page import TodosPage


def test_add_todo_appears_in_list(page: Page, app_url: str):
    """Ajouter une tâche la fait apparaître dans la liste"""
    todos = TodosPage(page)
    todos.navigate()
    todos.add_todo("Faire les courses")
    assert todos.get_visible_count() == 1
    expect(page.get_by_text("Faire les courses")).to_be_visible()


def test_mark_done_removes_from_active_filter(page: Page, app_url: str):
    """Marquer une tâche comme terminée la retire du filtre Actives"""
    todos = TodosPage(page)
    todos.navigate()
    todos.add_todo("Appeler le médecin")
    todos.mark_done("Appeler le médecin")
    todos.set_filter("active")
    assert todos.is_empty()


def test_delete_todo_removes_it(page: Page, app_url: str):
    """Supprimer une tâche la retire de la liste"""
    todos = TodosPage(page)
    todos.navigate()
    todos.add_todo("Tâche à supprimer")
    todos.delete_todo("Tâche à supprimer")
    assert todos.is_empty()

def test_empty_page_shows_empty_message(page: Page, app_url: str):
    """Naviguer sans tâche affiche le message vide"""
    todos = TodosPage(page)
    todos.navigate()

    assert todos.is_empty() == True

def test_delete_one_of_three_leaves_two(page: Page, app_url: str):
    """Supprimer une tache sur 3 et verifier qu il en reste 2"""
    todos = TodosPage(page)
    todos.navigate()
    todos.add_todo("Manger")
    todos.add_todo("Boire")
    todos.add_todo("Dormir")
    assert todos.get_visible_count() == 3
    todos.delete_todo("Dormir")
    assert todos.get_visible_count() == 2


    # à toi