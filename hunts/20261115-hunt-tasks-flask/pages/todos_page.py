from playwright.sync_api import Page


class TasksPage:
    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def add_task(self, title: str) -> None:
        self.page.get_by_label("Nouvelle tâche").fill(title)
        self.page.get_by_role("button", name="Ajouter").click()

    def get_pending_count_text(self) -> str:
        return self.page.locator("#pending-count").inner_text()

    def get_task_titles(self) -> list[str]:
        return self.page.locator("#task-list .task-title").all_inner_texts()

    def mark_done(self, title: str) -> None:
        row = self.page.locator("#task-list li").filter(has_text=title)
        row.get_by_role("button", name="Marquer comme fait").click()

    def get_empty_message(self) -> str:
        return self.page.locator("#empty-tasks").inner_text()