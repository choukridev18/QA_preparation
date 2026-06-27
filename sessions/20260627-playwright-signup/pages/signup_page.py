from playwright.sync_api import Page


class Step1Page:
    """
    Page Object pour le formulaire d'inscription — Étape 1.
    URL : http://localhost:5001/signup/step1
    Champs : Nom complet, Adresse email, Mot de passe
    Bouton  : Continuer
    """

    URL = "http://127.0.0.1:5001/signup/step1"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers l'étape 1
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le champ Nom complet
    # ----------------------------------------------------------
    # Entrée  : "Alice Dupont"
    # Attendu : le champ Nom complet contient "Alice Dupont"
    # ----------------------------------------------------------
    def fill_name(self, value: str) -> None:
        self.page.get_by_label("Nom complet").fill(value)

    # ----------------------------------------------------------
    # TODO 3 — Remplir le champ Adresse email
    # ----------------------------------------------------------
    # Entrée  : "alice@example.com"
    # ----------------------------------------------------------
    def fill_email(self, value: str) -> None:
        self.page.get_by_label("Adresse email").fill(value)

    # ----------------------------------------------------------
    # TODO 4 — Remplir le champ Mot de passe
    # ----------------------------------------------------------
    # Entrée  : "secret123"
    # ----------------------------------------------------------
    def fill_password(self, value: str) -> None:
        self.page.get_by_label("Mot de passe").fill(value)

    # ----------------------------------------------------------
    # TODO 5 — Cliquer sur le bouton Continuer
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Continuer").click()

    # ----------------------------------------------------------
    # TODO 6 — Lire le message d'erreur
    # ----------------------------------------------------------
    # Sortie  : "Le nom est obligatoire." (ou autre message)
    # ----------------------------------------------------------
    def get_error(self) -> str:
        return self.page.locator("#error-message").inner_text()


class Step2Page:
    """
    Page Object pour le formulaire d'inscription — Étape 2.
    URL : http://localhost:5001/signup/step2
    Champs  : checkbox Newsletter, select Langue
    Liens   : Retour à l'étape 1
    Bouton  : Terminer l'inscription
    """

    URL = "http://127.0.0.1:5001/signup/step2"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 7 — Cocher la case Newsletter
    # ----------------------------------------------------------
    # Attendu : la case "Recevoir la newsletter" est cochée
    # ----------------------------------------------------------
    def check_newsletter(self) -> None:
        self.page.get_by_role("checkbox", name="newsletter").check()

    # ----------------------------------------------------------
    # TODO 8 — Sélectionner une langue
    # ----------------------------------------------------------
    # Entrée  : "en" (valeur de l'option, pas le texte affiché)
    # ----------------------------------------------------------
    def select_language(self, value: str) -> None:
        self.page.locator("#language").select_option(value)

    # ----------------------------------------------------------
    # TODO 9 — Cliquer sur "Retour à l'étape 1"
    # ----------------------------------------------------------
    def go_back(self) -> None:
        self.page.get_by_role("link", name="Retour à l'étape 1").click()

    # ----------------------------------------------------------
    # TODO 10 — Cliquer sur "Terminer l'inscription"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Terminer l'inscription").click()


class ConfirmPage:
    """
    Page Object pour la page de confirmation.
    URL : http://localhost:5001/signup/confirm
    """

    URL = "http://127.0.0.1:5001/signup/confirm"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 11 — Lire le message de confirmation
    # ----------------------------------------------------------
    # Sortie  : "Bienvenue, Alice Dupont ! Votre compte a été créé avec succès."
    # ----------------------------------------------------------
    def get_confirm_message(self) -> str:
        return self.page.locator("#confirm-message").inner_text()

    def click_create_another_count(self) -> None:
        self.page.get_by_role("link", name="Créer un autre compte").click()
