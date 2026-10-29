from playwright.sync_api import Page


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
