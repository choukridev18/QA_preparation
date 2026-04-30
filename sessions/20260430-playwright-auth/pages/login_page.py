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
    # Indice : self.page.goto(self.URL)
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le formulaire et soumettre
    # ----------------------------------------------------------
    # Entrée  : email="alice@example.com", password="password123"
    # Attendu : le formulaire est soumis (Flask gère la redirection)
    # Indice  : get_by_label("Adresse email") pour le champ email
    #           get_by_label("Mot de passe") pour le champ password
    #           get_by_role("button", name="Se connecter") pour soumettre
    # ----------------------------------------------------------
    def login(self, email: str, password: str) -> None:
        self.page.get_by_label("Adresse email").fill(email)
        self.page.get_by_label("Mot de passe").fill(password)
        self.page.get_by_role("button",name = "Se connecter").click()


    # ----------------------------------------------------------
    # TODO 3 — Lire le message d'erreur affiché
    # ----------------------------------------------------------
    # Sortie  : le texte du message d'erreur (ex: "Identifiants incorrects...")
    #           ou None si aucun message n'est affiché
    # Indice  : locator("#error-message") — l'élément n'existe que si error=True
    #           .text_content() retourne le texte, .count() permet de vérifier l'existence
    # ----------------------------------------------------------
    def get_error_message(self) -> str | None:
        el = self.page.locator("#error-message")
        if el.count()== 0:
            return None
        else:
            return el.text_content()
