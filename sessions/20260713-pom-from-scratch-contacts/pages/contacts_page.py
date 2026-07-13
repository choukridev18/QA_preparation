from playwright.sync_api import Page


class Contacts:

    URL = "http://127.0.0.1:5001/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def search_contacts(self, value: str) -> None:
        self.page.get_by_label("Rechercher par nom").fill(value)
        self.page.get_by_role("button", name="Rechercher").click()

    def add_contact(self, nom: str, email: str, phone: str) -> None:
        self.page.get_by_label("Nom complet").fill(nom)
        self.page.get_by_label("Adresse email").fill(email)
        self.page.get_by_label("Téléphone").fill(phone)
        self.page.get_by_role("button", name="Ajouter").click()

    def delete_contact(self, nom) -> None:
        self.page.get_by_role("button", name=f"Supprimer {nom}").click()

    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()
