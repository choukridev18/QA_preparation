from playwright.sync_api import Page


class LeaveFormPage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        """Constructeur"""
        self.page = page

    def navigate(self) -> None:
        """permet la navigation"""
        self.page.goto(self.URL)

    def fill_start_date(self, start_date: str) -> None:
        """remplit la date de depart au format 'AAAA-MM-JJ'"""
        self.page.get_by_label("Date de début").fill(start_date)

    def fill_end_date(self, end_date: str) -> None:
        """remplit la date de fin au format 'AAAA-MM-JJ'"""
        self.page.get_by_label("Date de fin").fill(end_date)

    def fill_reason(self, reason: str) -> None:
        """remplit le champ motif"""
        self.page.get_by_label("Motif").fill(reason)

    def click_submit_form(self) -> None:
        """envoyer la demande"""
        self.page.get_by_role("button", name="Envoyer la demande").click()

    def get_error_message(self) -> str:
        """un message d'erreur s'affiche"""
        return self.page.locator("#error-message").inner_text()
