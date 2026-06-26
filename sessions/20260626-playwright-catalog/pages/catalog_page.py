from playwright.sync_api import Page


class CatalogPage:
    """
    Page Object pour le catalogue produits.
    URL : http://localhost:5001/
    """

    URL = "http://localhost:5001/"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Remplir le champ de recherche
    # ----------------------------------------------------------
    # Entrée  : "Laptop"
    # Attendu : le champ contient "Laptop"
    # ----------------------------------------------------------
    def fill_search(self, query: str) -> None:
        self.page.get_by_label("Rechercher").fill(query)

    # ----------------------------------------------------------
    # TODO 3 — Sélectionner une catégorie dans le menu déroulant
    # ----------------------------------------------------------
    # Entrée  : "Informatique"
    # Attendu : la catégorie est sélectionnée dans le <select>
    # ----------------------------------------------------------
    def select_category(self, category: str) -> None:
        self.page.get_by_label("Catégorie").select_option(category)

    # ----------------------------------------------------------
    # TODO 4 — Soumettre le formulaire de recherche
    # ----------------------------------------------------------
    def submit_search(self) -> None:
        self.page.get_by_role("button", name="Rechercher").click()

    # ----------------------------------------------------------
    # TODO 5 — Réinitialiser les filtres
    # ----------------------------------------------------------
    # Attendu : retour à la liste complète (lien "Réinitialiser")
    # ----------------------------------------------------------
    def reset_filters(self) -> None:
        self.page.get_by_role("link", name="Réinitialiser").click()

    # ----------------------------------------------------------
    # TODO 6 — Lire le nombre de résultats affichés
    # ----------------------------------------------------------
    # Sortie  : 6  (si "6 produit(s) trouvé(s)" est affiché)
    # ----------------------------------------------------------
    def get_result_count(self) -> int:
        return int(self.page.locator("#result-count").inner_text().split()[0])

    # ----------------------------------------------------------
    # TODO 7 — Lire les noms de tous les produits affichés
    # ----------------------------------------------------------
    # Sortie  : ["Laptop Pro", "Souris sans fil", ...]
    # ----------------------------------------------------------
    def get_product_names(self) -> list[str]:
        return self.page.locator(".product-name").all_inner_texts()

    # ----------------------------------------------------------
    # TODO 8 — Vérifier si le message "Aucun produit" est affiché
    # ----------------------------------------------------------
    # Sortie  : True si aucun résultat, False sinon
    # ----------------------------------------------------------
    def has_no_results_message(self) -> bool:
        return self.page.locator("#no-results").count() > 0
