from playwright.sync_api import Page, expect


class SupportPage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def fill_field_subject(self, sujet) -> None:
        """Rempli le champs sujet"""
        self.page.get_by_label("Sujet").fill(sujet)

    def choice_priority(self, option) -> None:
        """ " Permet de selectionner une option"""
        self.page.get_by_label("Priorité").select_option(option)

    def write_in_field_message(self, message) -> None:
        """permet d'ecrire le message"""
        self.page.get_by_label("Description").fill(message)

    def submit(self) -> None:
        """cliquer sur le bouton créer le ticket"""
        self.page.get_by_role("button", name="Créer le ticket").click()

    def get_visibility_tickets(self) -> list:
        """les tickets visibles"""
        return self.page.locator("#ticket-list .ticket-subject").all_inner_texts()

    def get_message_success_creation(self) -> str:
        """retourne le message succes d un ticket crée"""
        return self.page.locator("#success-message").inner_text()

    def get_empty_message_ticket(self) -> str:
        return self.page.locator("#empty-tickets").inner_text()
