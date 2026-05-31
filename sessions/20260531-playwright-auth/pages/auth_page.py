from os import name
from playwright.sync_api import Page


class AuthPage:
    """
    Page Object pour l'authentification.
    Login : http://localhost:5001/login
    Dashboard : http://localhost:5001/dashboard
    """

    URL = "http://localhost:5001/login"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page de login
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le formulaire de login
    # ----------------------------------------------------------
    # Entrée  : email="admin@example.com", password="password123"
    # Attendu : champs remplis
    # Indice  : les inputs ont les labels "Adresse email" et "Mot de passe"
    # ----------------------------------------------------------
    def fill_login(self, email: str, password: str) -> None:
        self.page.get_by_label("Adresse email").fill(email)
        self.page.get_by_label("Mot de passe").fill(password)

    # ----------------------------------------------------------
    # TODO 3 — Soumettre le formulaire
    # ----------------------------------------------------------
    # Attendu : clic sur "Se connecter"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Se connecter").click()

    # ----------------------------------------------------------
    # TODO 4 — Lire le message d'erreur
    # ----------------------------------------------------------
    # Sortie  : texte de #error-message, ou "" si absent
    # Indice  : utilise is_visible() avant inner_text()
    # ----------------------------------------------------------
    def get_error_message(self) -> str:
        msg = self.page.locator("#error-message")
        if msg.is_visible():
            return msg.inner_text()
        else:
            return ""

    # ----------------------------------------------------------
    # TODO 5 — Lire le message de bienvenue sur le dashboard
    # ----------------------------------------------------------
    # Sortie  : texte de #welcome-message
    # ----------------------------------------------------------
    def get_welcome_message(self) -> str:
        return self.page.locator("#welcome-message").inner_text()

    # ----------------------------------------------------------
    # TODO 6 — Se déconnecter
    # ----------------------------------------------------------
    # Attendu : clic sur "Se déconnecter"
    # ----------------------------------------------------------
    def logout(self) -> None:
        self.page.get_by_role("button", name="Se déconnecter").click()
