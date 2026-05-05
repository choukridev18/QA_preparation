from playwright.sync_api import Page


class ProfilePage:
    """
    Page Object pour la page de profil utilisateur.
    URL : http://localhost:5001/profile
    """

    URL = "http://localhost:5001/profile"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page de profil
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le champ Nom complet
    # ----------------------------------------------------------
    def fill_name(self, value: str) -> None:
        self.page.get_by_label("Nom complet").fill(value)

    # ----------------------------------------------------------
    # TODO 3 — Remplir le champ Email
    # ----------------------------------------------------------
    def fill_email(self, value: str) -> None:
        self.page.get_by_label("Email").fill(value)

    # ----------------------------------------------------------
    # TODO 4 — Cliquer sur le bouton Enregistrer
    # ----------------------------------------------------------
    def click_save(self) -> None:
        self.page.get_by_role("button",name="Enregistrer").click()

    # ----------------------------------------------------------
    # TODO 5 — Lire le message de succès
    # ----------------------------------------------------------
    def get_success_message(self) -> str:
        return self.page.locator("#success-message").inner_text()

    # ----------------------------------------------------------
    # TODO 6 — Lire le message d'erreur
    # ----------------------------------------------------------
    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()

    
    # ----------------------------------------------------------
    # TODO 7 — Lire la valeur courante du champ Nom complet
    # ----------------------------------------------------------
    def get_name_value(self) -> str:
        return self.page.get_by_label("Nom complet").input_value()
