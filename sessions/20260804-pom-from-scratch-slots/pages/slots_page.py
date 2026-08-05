from playwright.sync_api import Page


class SlotsPage:

    URL = "http://127.0.0.1:5001/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def choice_one_slot(self, label: str) -> None:
        self.page.get_by_label(label, exact=True).check()

    def submit_slot(self) -> None:
        self.page.get_by_role("button", name="Réserver").click()

    def cancel_booking(self) -> None:
        self.page.locator("#cancel-button").click()

    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()


class ConfirmationPage:

    URL = "http://127.0.0.1:5001/confirmation/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, slot: str) -> None:
        self.page.goto(f"{self.URL}{slot}")

    def get_slot_label(self) -> str:
        return self.page.locator("#slot-label").inner_text()

    def return_main_page(self) -> None:
        self.page.get_by_role("link", name="Retour à la liste").click()
