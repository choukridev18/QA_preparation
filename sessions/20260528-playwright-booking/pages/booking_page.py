from os import name
from playwright.sync_api import Page


class BookingPage:
    """
    Page Object pour le formulaire de réservation multi-étapes.
    Étape 1 : http://localhost:5001/step1
    Étape 2 : http://localhost:5001/step2
    Confirmation : http://localhost:5001/confirm
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
    # TODO 2 — Remplir le formulaire de l'étape 1
    # ----------------------------------------------------------
    # Entrée  : name="Jean Dupont", email="jean@example.com"
    # Attendu : champs remplis, formulaire prêt à être soumis
    # Indice  : les inputs ont les labels "Prénom et nom" et "Adresse email"
    # ----------------------------------------------------------
    def fill_step1(self, name: str, email: str) -> None:
        self.page.get_by_label("Prénom et nom").fill(name)
        self.page.get_by_label("Adresse email").fill(email)

    # ----------------------------------------------------------
    # TODO 3 — Soumettre l'étape 1 pour passer à l'étape 2
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton "Étape suivante", navigation vers /step2
    # ----------------------------------------------------------
    def submit_step1(self) -> None:
        self.page.get_by_role("button", name="Étape suivante").click()

    # ----------------------------------------------------------
    # TODO 4 — Remplir le formulaire de l'étape 2
    # ----------------------------------------------------------
    # Entrée  : date="15/07/2026", guests=3
    # Attendu : champs remplis
    # Indice  : l'input date a le label "Date de réservation"
    #           le select a le label "Nombre de personnes"
    #           pour le select, utilise select_option(str(guests))
    # ----------------------------------------------------------
    def fill_step2(self, date: str, guests: int) -> None:
        self.page.get_by_label("Date de réservation").fill(date)
        self.page.get_by_label("Nombre de personnes").select_option(str(guests))

    # ----------------------------------------------------------
    # TODO 5 — Soumettre l'étape 2 pour passer à la confirmation
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton "Étape suivante", navigation vers /confirm
    # ----------------------------------------------------------
    def submit_step2(self) -> None:
        self.page.get_by_role("button", name="Étape suivante").click()

    # ----------------------------------------------------------
    # TODO 6 — Lire le nom affiché dans le récapitulatif
    # ----------------------------------------------------------
    # Sortie  : ex. "Jean Dupont"
    # Indice  : le nom est dans l'élément #summary-name
    # ----------------------------------------------------------
    def get_summary_name(self) -> str:
        return self.page.locator("#summary-name").inner_text()

    # ----------------------------------------------------------
    # TODO 7 — Confirmer la réservation
    # ----------------------------------------------------------
    # Attendu : clic sur "Confirmer la réservation", navigation vers /done
    # ----------------------------------------------------------
    def confirm(self) -> None:
        self.page.get_by_role("button", name="Confirmer la réservation").click()

    # ----------------------------------------------------------
    # TODO 8 — Lire le message de succès
    # ----------------------------------------------------------
    # Sortie  : texte de l'élément #success-message
    # ----------------------------------------------------------
    def get_success_message(self) -> str:
        return self.page.locator("#success-message").inner_text()

    # ----------------------------------------------------------
    # TODO 9 — Lire le message d'erreur
    # ----------------------------------------------------------
    # Sortie  : texte de l'élément #error-message (ou "" si absent)
    # Indice  : utilise is_visible() avant inner_text() pour éviter une erreur
    # ----------------------------------------------------------
    def get_error_message(self) -> str:
        msg_error = self.page.locator("#error-message")
        if msg_error.is_visible():
            return msg_error.inner_text()
        else:
            return ""

    def get_summary_guests(self) -> str:
        return self.page.locator("#summary-guests").inner_text()
