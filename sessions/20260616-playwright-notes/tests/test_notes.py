import pytest
from playwright.sync_api import Page, expect
from pages.notes_page import NotesListPage, NewNotePage, EditNotePage


def test_list_shows_default_notes(page: Page):
    """La liste affiche les 2 notes par défaut."""
    p = NotesListPage(page)
    p.navigate()
    assert p.get_note_count() == 2


def test_create_note_adds_to_list(page: Page):
    """Créer une note la fait apparaître dans la liste."""
    new = NewNotePage(page)
    new.navigate()
    new.fill_title("Ma nouvelle note")
    new.fill_content("Contenu de test.")
    new.submit()
    p = NotesListPage(page)
    assert "Ma nouvelle note" in p.get_note_titles()


def test_create_note_empty_title_shows_error(page: Page):
    """Soumettre sans titre affiche un message d'erreur."""
    new = NewNotePage(page)
    new.navigate()
    new.fill_content("Contenu sans titre.")
    new.submit()
    assert new.get_title_error() == "Le titre est obligatoire."


def test_delete_note_removes_from_list(page: Page):
    """Supprimer une note diminue le compteur."""
    p = NotesListPage(page)
    p.navigate()
    p.delete_note(1)
    assert p.get_note_count() == 1


def test_edit_note_updates_title(page: Page):
    """Modifier le titre d'une note met à jour la liste."""
    p = NotesListPage(page)
    p.navigate()
    p.edit_note(1)
    edit = EditNotePage(page)
    edit.fill_title("Titre modifié")
    edit.fill_content("Nouveau contenu.")
    edit.submit()
    assert "Titre modifié" in p.get_note_titles()


def test_note_without_message_shows_error_message(page: Page):
    """Créer une note sans contenu affiche un message d erreur"""
    new = NewNotePage(page)
    new.navigate()
    new.fill_title("test_titre")
    new.fill_content("")
    new.submit()
    assert new.get_content_error() == "Le contenu est obligatoire."


def test_cancel_creation_redirect_main(page: Page):
    """Cliquer sur annuler redirige vers la liste"""
    new = NewNotePage(page)
    new.navigate()
    new.cancel()
    expect(page).to_have_url(NotesListPage.URL)
