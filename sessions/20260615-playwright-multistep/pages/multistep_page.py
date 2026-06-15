from asyncio import Semaphore
from playwright.sync_api import Page


class Step1Page:
    """
    Page Object pour l'étape 1 — Informations personnelles.
    URL : http://localhost:5001/step1
    """

    URL = "http://localhost:5001/step1"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers l'étape 1
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le champ "Prénom"
    # ----------------------------------------------------------
    def fill_first_name(self, value: str) -> None:
        self.page.get_by_label("Prénom", exact=True).fill(value)

    # ----------------------------------------------------------
    # TODO 3 — Remplir le champ "Nom"
    # ----------------------------------------------------------
    def fill_last_name(self, value: str) -> None:
        self.page.get_by_label("Nom", exact=True).fill(value)

    # ----------------------------------------------------------
    # TODO 4 — Remplir le champ "Email"
    # ----------------------------------------------------------
    def fill_email(self, value: str) -> None:
        self.page.get_by_label("Email").fill(value)

    # ----------------------------------------------------------
    # TODO 5 — Cliquer sur "Suivant"
    # ----------------------------------------------------------
    # Attendu : soumet le formulaire et navigue vers /step2
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Suivant").click()

    # ----------------------------------------------------------
    # TODO 6 — Lire le message d'erreur du champ "Prénom"
    # ----------------------------------------------------------
    # Sortie : ex. "Le prénom est requis." — chaîne vide si absent
    # ----------------------------------------------------------
    def get_first_name_error(self) -> str:
        return self.page.locator("#error-first-name").inner_text()

    def get_last_name_error(self) -> str:
        return self.page.locator("#error-last-name").inner_text()

    # ----------------------------------------------------------
    # TODO 7 — Lire le message d'erreur du champ "Email"
    # ----------------------------------------------------------
    # Sortie : ex. "Un email valide est requis."
    # ----------------------------------------------------------
    def get_email_error(self) -> str:
        return self.page.locator("#error-email").inner_text()

    def get_all_errors(self) -> list[str]:
        return self.page.locator("[role='alert']").all_inner_texts()


class Step2Page:
    """
    Page Object pour l'étape 2 — Choix du plan.
    URL : http://localhost:5001/step2
    """

    URL = "http://localhost:5001/step2"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 8 — Naviguer vers l'étape 2
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 9 — Sélectionner un plan
    # ----------------------------------------------------------
    # Entrée  : plan="Pro"
    # Indice  : c'est un <select> — utilise select_option()
    # ----------------------------------------------------------
    def select_plan(self, plan: str) -> None:
        self.page.get_by_label("Plan").select_option(plan)

    # ----------------------------------------------------------
    # TODO 10 — Cliquer sur "Suivant"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Suivant").click()

    # ----------------------------------------------------------
    # TODO 11 — Cliquer sur "Retour"
    # ----------------------------------------------------------
    # Attendu : retourne sur /step1
    # ----------------------------------------------------------
    def go_back(self) -> None:
        self.page.get_by_role("link", name="Retour").click()

    # ----------------------------------------------------------
    # TODO 12 — Lire le message d'erreur du champ "Plan"
    # ----------------------------------------------------------
    # Sortie : ex. "Choisissez un plan valide."
    # ----------------------------------------------------------
    def get_plan_error(self) -> str:
        return self.page.locator("#error-plan").inner_text()


class ConfirmPage:
    """
    Page Object pour l'étape 3 — Confirmation.
    URL : http://localhost:5001/confirm
    """

    URL = "http://localhost:5001/confirm"

    def __init__(self, page: Page):
        self.page = page

    def get_last_name(self) -> str:
        return self.page.locator("#summary-last-name").inner_text()

    # ----------------------------------------------------------
    # TODO 13 — Lire le prénom affiché dans le récapitulatif
    # ----------------------------------------------------------
    # Sortie : ex. "Alice"
    # ----------------------------------------------------------
    def get_first_name(self) -> str:
        return self.page.locator("#summary-first-name").inner_text()

    # ----------------------------------------------------------
    # TODO 14 — Lire le plan affiché dans le récapitulatif
    # ----------------------------------------------------------
    # Sortie : ex. "Pro"
    # ----------------------------------------------------------
    def get_plan(self) -> str:
        return self.page.locator("#summary-plan").inner_text()

    # ----------------------------------------------------------
    # TODO 15 — Cliquer sur "Confirmer l'inscription"
    # ----------------------------------------------------------
    # Attendu : soumet et navigue vers /success
    # ----------------------------------------------------------
    def confirm(self) -> None:
        self.page.get_by_role("button", name="Confirmer l'inscription").click()
