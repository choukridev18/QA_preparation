from playwright.sync_api import Page


class Vote:
    URL = "http://127.0.0.1:5001/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def choice_langage(self, language: str) -> None:
        self.page.get_by_label(language, exact=True).check()

    def submit_vote(self) -> None:
        self.page.get_by_role("button", name="Voter").click()

    def shows_results(self) -> None:
        self.page.get_by_role("link", name="Voir les résultats sans voter").click()

    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()


class Results:

    URL = "http://127.0.0.1:5001/results"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def click_vote_again(self) -> None:
        self.page.get_by_role("link", name="Voter à nouveau").click()

    def get_total_vote(self) -> str:
        return self.page.locator("#total-votes").inner_text()

    def get_results_list(self) -> str:
        return self.page.locator("#results-list").all_inner_texts()
