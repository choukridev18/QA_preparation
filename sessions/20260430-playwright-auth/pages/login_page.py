from playwright.sync_api import Page


class LoginPage:
    """
    Page Object pour la page de connexion.
    URL : http://localhost:5001/login
    """

    URL = "http://localhost:5001/login"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page de connexion
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le formulaire et soumettre
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    def login(self, email: str, password: str) -> None:
        self.page.get_by_label("Adresse email").fill(email)
        self.page.get_by_label("Mot de passe").fill(password)
        self.page.get_by_role("button",name = "Se connecter").click()


    # ----------------------------------------------------------
    # TODO 3 — Lire le message d'erreur affiché
    # ----------------------------------------------------------
    #           ou None si aucun message n'est affiché
    # ----------------------------------------------------------
    def get_error_message(self) -> str | None:
        el = self.page.locator("#error-message")
        if el.count()== 0:
            return None
        else:
            return el.text_content()
