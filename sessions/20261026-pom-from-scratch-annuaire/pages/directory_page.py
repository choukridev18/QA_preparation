from playwright.sync_api import Page


class DirectoryPage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def get_result_count(self) -> int:
        return self.page.locator("#results li").count()

    def fill_search_name(self, name: str) -> None:
        self.page.get_by_label("Recherche").fill(name)

    def submit(self) -> None:
        self.page.get_by_role("button", name="Rechercher").click()

    def get_empty_message(self) -> str:
        return self.page.locator("#empty-message").inner_text()

    def search(self, name: str) -> None:
        self.fill_search_name(name)
        self.submit()

    def get_result_names(self) -> list[str]:
        return self.page.locator("#results li").all_inner_texts()

    def is_colleague_displayed(self, name: str) -> bool:
        return self.page.get_by_role("listitem", name=name).count() > 0
