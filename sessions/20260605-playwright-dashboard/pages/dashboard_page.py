from playwright.sync_api import Page


class DashboardPage:
    """
    Page Object pour le tableau de bord des tickets avec filtres.
    URL : http://localhost:5001/dashboard
    """

    URL = "http://localhost:5001/dashboard"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers le tableau de bord
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Sélectionner un statut dans le filtre
    # ----------------------------------------------------------
    # Entrée  : "ouvert", "en_cours", "ferme" ou "" pour Tous
    # Attendu : la valeur est sélectionnée dans le <select id="status">
    # ----------------------------------------------------------
    def set_status_filter(self, status: str) -> None:
        self.page.get_by_label("Statut").select_option(status)

    # ----------------------------------------------------------
    # TODO 3 — Sélectionner une priorité dans le filtre
    # ----------------------------------------------------------
    # Entrée  : "haute", "basse" ou "" pour Toutes
    # ----------------------------------------------------------
    def set_priority_filter(self, priority: str) -> None:
        self.page.get_by_label("Priorité").select_option(priority)

    # ----------------------------------------------------------
    # TODO 4 — Saisir un texte dans le champ recherche
    # ----------------------------------------------------------
    # Entrée  : ex. "connexion"
    # ----------------------------------------------------------
    def set_search(self, text: str) -> None:
        self.page.get_by_label("Recherche").fill(text)

    # ----------------------------------------------------------
    # TODO 5 — Soumettre le formulaire de filtres
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton « Appliquer les filtres »
    # ----------------------------------------------------------
    def apply_filters(self) -> None:
        self.page.get_by_role("button", name="Appliquer les filtres").click()

    # ----------------------------------------------------------
    # TODO 6 — Réinitialiser tous les filtres
    # ----------------------------------------------------------
    # Attendu : clic sur le lien « Réinitialiser les filtres »
    # ----------------------------------------------------------
    def reset_filters(self) -> None:
        self.page.get_by_role("link", name="Réinitialiser les filtres").click()

    # ----------------------------------------------------------
    # TODO 7 — Lire le nombre de tickets affichés
    # ----------------------------------------------------------
    # Sortie  : entier extrait de « X ticket(s) affiché(s) » (#ticket-count)
    # ----------------------------------------------------------
    def get_displayed_count(self) -> int:
        nbr = self.page.locator("#ticket-count").inner_text()
        chiffre = nbr.split()[0]
        resul = int(chiffre)
        return resul

    # ----------------------------------------------------------
    # TODO 8 — Lire les titres des tickets visibles dans le tableau
    # ----------------------------------------------------------
    # Sortie  : liste de str, ex. ["Bug connexion impossible", ...]
    # ----------------------------------------------------------
    def get_visible_titles(self) -> list[str]:
        return self.page.locator(".ticket-title").all_inner_texts()
