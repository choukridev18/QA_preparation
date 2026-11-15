from playwright.sync_api import Page, expect
from pages.todos_page import TasksPage


# --- tests corrects (ne pas casser) ---


def test_add_form_visible(page: Page):
    page.goto(TasksPage.URL)
    expect(page.get_by_label("Nouvelle tâche")).to_be_visible()
    expect(page.get_by_role("button", name="Ajouter")).to_be_visible()


def test_empty_list_shows_message(page: Page):
    tasks = TasksPage(page)
    tasks.navigate()
    assert tasks.get_empty_message() == "Aucune tâche pour le moment."


def test_add_task_appears_in_list(page: Page):
    tasks = TasksPage(page)
    tasks.navigate()
    tasks.add_task("Préparer la réunion")
    assert "Préparer la réunion" in tasks.get_task_titles()


# --- tests avec 1 bug chacun (à corriger ici) ---


def test_pending_count_after_one_task(page: Page):
    tasks = TasksPage(page)
    tasks.navigate()
    tasks.add_task("Appeler le client")
    assert tasks.get_pending_count_text() == "À faire : 1"


def test_add_task_via_css_id(page: Page):
    page.goto(TasksPage.URL)
    page.get_by_label("Nouvelle tâche").fill("Répondre au mail")
    page.get_by_role("button", name="Ajouter").click()
    tasks = TasksPage(page)
    assert "Répondre au mail" in tasks.get_task_titles()


def test_mark_task_done_updates_count(page: Page):
    tasks = TasksPage(page)
    tasks.navigate()
    tasks.add_task("Ranger le bureau")
    tasks.mark_done("Ranger le bureau")
    assert tasks.get_pending_count_text() == "À faire : 0"


def test_task_line_shows_title_only(page: Page):
    tasks = TasksPage(page)
    tasks.navigate()
    tasks.add_task("Acheter du lait")
    line = page.locator("#task-list li .task-title").first
    expect(line).to_have_text("Acheter du lait")
