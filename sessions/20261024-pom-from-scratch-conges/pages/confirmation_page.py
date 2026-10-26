from playwright.sync_api import Page


class ConfirmationPage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        """Constructeur"""
        self.page = page

    def navigate(self) -> None:
        """navigation page confirmation"""
        self.page.goto(f"{self.URL}/confirmation")

    def get_message_leaving_recorded(self) -> str:
        """message de demande enregistré"""
        return self.page.get_by_role("heading", name="Demande enregistrée").inner_text()

    def get_message_confirmation_start_date(self) -> str:
        """confirmation de date de debut"""
        return self.page.locator("#confirm-start").inner_text()

    def get_message_confirmation_end_date(self) -> str:
        """confirmation de date de fin"""
        return self.page.locator("#confirm-end").inner_text()

    def get_message_confirmation_reason(self) -> str:
        """confirmation de la raison"""
        return self.page.locator("#confirm-reason").inner_text()

    def click_new_request(self) -> None:
        """nouvelle demande"""
        self.page.get_by_role("link", name="Nouvelle demande").click()
