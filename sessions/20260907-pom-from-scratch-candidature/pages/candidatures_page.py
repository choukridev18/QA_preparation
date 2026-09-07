from playwright.sync_api import Page


class Step1Page:
    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(f"{self.URL}/step1")

    def fill_name(self, value: str) -> None:
        self.page.get_by_label("Nom complet").fill(value)

    def fill_email(self, email: str) -> None:
        self.page.get_by_label("Adresse email").fill(email)

    def fill_number_phone(self, phone: str) -> None:
        self.page.get_by_label("Téléphone").fill(phone)

    def submit(self):
        self.page.get_by_role("button", name="Suivant").click()

    def get_message_error(self) -> str:
        return self.page.locator("#error-message").inner_text()


class Step2Page:
    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(f"{self.URL}/step2")

    def choice_position(self, value: str) -> None:
        self.page.get_by_label("Poste visé").select_option(value)

    def experiences_years(self, value: str) -> None:
        self.page.get_by_label("Années d'expérience").select_option(value)

    def motivation(self, text: str) -> None:
        self.page.get_by_label("Lettre de motivation").fill(text)

    def submit(self) -> None:
        self.page.get_by_role("button", name="Envoyer ma candidature").click()

    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()


class ConfirmationPage:
    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(f"{self.URL}/confirmation")

    def message_success(self) -> str:
        return self.page.locator("#confirm-message").inner_text()

    def click_new_application(self) -> None:
        self.page.get_by_role("link", name="Soumettre une nouvelle candidature").click()
