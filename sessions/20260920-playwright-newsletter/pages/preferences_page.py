from playwright.sync_api import Page


class PreferencesPage:
    """
    Page Object pour les préférences newsletter.
    URL : http://127.0.0.1:5001/preferences
    """

    URL = "http://127.0.0.1:5001/preferences"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page préférences
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir l'email
    # ----------------------------------------------------------
    # Entrée  : "alice@exemple.com"
    # Attendu : le champ email contient cette valeur
    # ----------------------------------------------------------
    def fill_email(self, email: str) -> None:
        self.page.get_by_label("Email").fill(email)

    # ----------------------------------------------------------
    # TODO 3 — Cocher une catégorie par son label visible
    # ----------------------------------------------------------
    # Entrée  : "Technologie" | "Culture" | "Sport"
    # Attendu : la case correspondante est cochée
    # ----------------------------------------------------------
    def check_category(self, label: str) -> None:
        self.page.get_by_label(label).check()

    # ----------------------------------------------------------
    # TODO 4 — Choisir une fréquence par son label visible
    # ----------------------------------------------------------
    # Entrée  : "Quotidienne" | "Hebdomadaire" | "Mensuelle"
    # Attendu : le radio correspondant est sélectionné
    # ----------------------------------------------------------
    def select_frequency(self, label: str) -> None:
        self.page.get_by_label(label).check()

    # ----------------------------------------------------------
    # TODO 5 — Soumettre le formulaire
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton "Enregistrer"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Enregistrer").click()

    # ----------------------------------------------------------
    # TODO 6 — Lire le message d'erreur
    # ----------------------------------------------------------
    # Sortie  : texte de #error-message (role="alert")
    # ----------------------------------------------------------
    def get_error_message(self) -> str:
        return self.page.locator("#error-message").inner_text()

    # ----------------------------------------------------------
    # TODO 7 — Lire le message de succès
    # ----------------------------------------------------------
    # Sortie  : texte de #success-message (role="status")
    # ----------------------------------------------------------
    def get_success_message(self) -> str:
        return self.page.locator("#success-message").inner_text()

    # ----------------------------------------------------------
    # TODO 8 — Lire l'email enregistré affiché dans le résumé
    # ----------------------------------------------------------
    # Sortie  : texte de #saved-email
    # ----------------------------------------------------------
    def get_saved_email(self) -> str:
        return self.page.locator("#saved-email").inner_text()

    def go_to_summary(self) -> None:
        self.page.get_by_role("link", name="Voir la page résumé").click()
