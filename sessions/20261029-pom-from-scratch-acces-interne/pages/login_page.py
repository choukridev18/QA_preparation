from playwright.sync_api import Page


class LoginPage:
    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def fill_email(self, email: str) -> None:
        self.page.get_by_label("Email professionnel").fill(email)

    def fill_password(self, password: str) -> None:
        self.page.get_by_label("Mot de passe").fill(password)

    def submit(self) -> None:
        self.page.get_by_role("button", name="Se connecter").click()

    def get_error_message(self) -> str:
        return self.page.locator("#login-error").inner_text()


class MemberPage:
    URL = "http://127.0.0.1:5001/member"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def get_welcome_message(self) -> str:
        return self.page.locator("#user-greeting").inner_text()

    def logout(self) -> None:
        self.page.get_by_role("button", name="Se déconnecter").click()
