from playwright.sync_api import Page, expect


class TicketListPage:
    """
    Page Object pour la liste des tickets de support.
    URL : http://localhost:5001/tickets
    """

    URL = "http://localhost:5001/tickets"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la liste des tickets
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Cliquer sur "Nouveau ticket"
    # ----------------------------------------------------------
    # Attendu : l'URL devient http://localhost:5001/tickets/new
    # ----------------------------------------------------------
    def go_to_new_ticket(self) -> None:
        self.page.get_by_role("link", name="Nouveau ticket").click()

    # ----------------------------------------------------------
    # TODO 3 — Lire le nombre de tickets ouverts
    # ----------------------------------------------------------
    # Sortie : ex. 2  (l'entier dans "#open-count-number")
    # ----------------------------------------------------------
    def get_open_count(self) -> int:
        return int(self.page.locator("#open-count-number").inner_text())

    # ----------------------------------------------------------
    # TODO 4 — Lire les titres de tous les tickets affichés
    # ----------------------------------------------------------
    # Sortie : ex. ["Login ne fonctionne pas", "Comment changer mon email ?"]
    # ----------------------------------------------------------
    def get_ticket_titles(self) -> list[str]:
        return self.page.locator(".ticket-title").all_inner_texts()

    # ----------------------------------------------------------
    # TODO 5 — Lire le statut d'un ticket par son ID
    # ----------------------------------------------------------
    # Entrée  : ticket_id=1
    # Sortie  : ex. "Ouvert" ou "Résolu"
    # ----------------------------------------------------------
    def get_ticket_status(self, ticket_id: int) -> str:
        return self.page.locator(f"#ticket-{ticket_id} .ticket-status").inner_text()

    # ----------------------------------------------------------
    # TODO 6 — Cliquer sur "Résolu" pour un ticket donné
    # ----------------------------------------------------------
    # Entrée  : ticket_id=1
    # Attendu : le formulaire de résolution est soumis
    # ----------------------------------------------------------
    def resolve_ticket(self, ticket_id: int) -> None:
        self.page.get_by_role("button", name=f"Résoudre le ticket {ticket_id}").click()


class NewTicketPage:
    """
    Page Object pour le formulaire de création de ticket.
    URL : http://localhost:5001/tickets/new
    """

    URL = "http://localhost:5001/tickets/new"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 7 — Naviguer vers le formulaire de création
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 8 — Remplir le champ "Titre"
    # ----------------------------------------------------------
    # Entrée  : title="Impossible de se connecter"
    # ----------------------------------------------------------
    def fill_title(self, title: str) -> None:
        self.page.get_by_label("Titre").fill(title)

    # ----------------------------------------------------------
    # TODO 9 — Sélectionner une catégorie
    # ----------------------------------------------------------
    # Entrée  : category="Bug"
    # Indice  : c'est un <select> — utilise select_option()
    # ----------------------------------------------------------
    def select_category(self, category: str) -> None:
        self.page.get_by_label("Catégorie").select_option(category)

    # ----------------------------------------------------------
    # TODO 10 — Remplir la description
    # ----------------------------------------------------------
    # Entrée  : description="Le bouton login ne répond pas."
    # ----------------------------------------------------------
    def fill_description(self, description: str) -> None:
        self.page.get_by_label("Description").fill(description)

    # ----------------------------------------------------------
    # TODO 11 — Soumettre le formulaire
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton "Soumettre"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Soumettre").click()

    # ----------------------------------------------------------
    # TODO 12 — Lire le message d'erreur du champ "Titre"
    # ----------------------------------------------------------
    # Sortie  : ex. "Le titre est requis." — chaîne vide si pas d'erreur
    # ----------------------------------------------------------
    def get_title_error(self) -> str:
        return self.page.locator("#error-title").inner_text()

    # ----------------------------------------------------------
    # TODO 13 — Lire le message d'erreur du champ "Catégorie"
    # ----------------------------------------------------------
    # Sortie  : ex. "Choisissez une catégorie valide." — chaîne vide si pas d'erreur
    # ----------------------------------------------------------
    def get_category_error(self) -> str:
        return self.page.locator("#error-category").inner_text()

    def submit_cancel(self) -> None:
        self.page.get_by_role("link", name="Annuler").click()
