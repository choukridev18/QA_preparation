from playwright.sync_api import Page


class DashboardPage:
    """
    Page Object pour le tableau de bord (accessible uniquement si connecté).
    URL : http://localhost:5001/dashboard
    """

    URL = "http://localhost:5001/dashboard"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer directement vers le dashboard
    # ----------------------------------------------------------
    # Indice : self.page.goto(self.URL)
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Lire le titre principal de la page
    # ----------------------------------------------------------
    # Sortie  : "Tableau de bord"
    # Indice  : get_by_role("heading", name="Tableau de bord")
    #           .text_content() retourne le texte de l'élément
    # ----------------------------------------------------------
    def get_title(self) -> str:
        return self.page.locator("h1").text_content()

    # ----------------------------------------------------------
    # TODO 3 — Lire le message de bienvenue
    # ----------------------------------------------------------
    # Sortie  : "Bienvenue, alice@example.com !"
    # Indice  : locator("#welcome-message").text_content()
    # ----------------------------------------------------------
    def get_welcome_message(self) -> str:
        return self.page.locator("#welcome-message").text_content()

    # ----------------------------------------------------------
    # TODO 4 — Cliquer sur le bouton de déconnexion
    # ----------------------------------------------------------
    # Attendu : la session est effacée, Flask redirige vers /login
    # Indice  : get_by_role("button", name="Se déconnecter")
    # ----------------------------------------------------------
    def logout(self) -> None:
        return self.page.get_by_role("button",name="Se déconnecter").click()
