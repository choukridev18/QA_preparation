from playwright.sync_api import Page


class CartPage:
    """
    Page Object pour la page panier.
    URL : http://localhost:5001/cart
    """

    URL = "http://localhost:5001/cart"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer directement vers la page panier
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Compter le nombre de lignes dans le tableau panier
    # ----------------------------------------------------------
    # Sortie  : entier, ex: 2 si deux articles dans le panier
    # Indice  : chaque article est une ligne <tr> dans le <tbody>
    # ----------------------------------------------------------
    def get_item_count(self) -> int:
        return self.page.locator("tbody tr").count()
        

    # ----------------------------------------------------------
    # TODO 3 — Modifier la quantité d'un article
    # ----------------------------------------------------------
    # Entrée  : product_name="Souris ergonomique", quantity=3
    # Attendu : formulaire soumis → redirection vers /cart
    # Indice  : l'input a un aria-label "Nouvelle quantité pour {product_name}"
    #           le bouton a un aria-label "Mettre à jour {product_name}"
    # ----------------------------------------------------------
    def update_quantity(self, product_name: str, quantity: int) -> None:
        self.page.get_by_label(f"Nouvelle quantité pour {product_name}").fill(str(quantity))
        self.page.get_by_role("button", name=f"Mettre à jour {product_name}").click()

    # ----------------------------------------------------------
    # TODO 4 — Supprimer un article du panier
    # ----------------------------------------------------------
    # Entrée  : product_name="Casque audio"
    # Attendu : article retiré du tableau (ou panier vide affiché)
    # Indice  : le bouton a un aria-label "Supprimer {product_name}"
    # ----------------------------------------------------------
    def remove_item(self, product_name: str) -> None:
        self.page.get_by_role("button",name=f"Supprimer {product_name}").click()

    # ----------------------------------------------------------
    # TODO 5 — Lire le total affiché
    # ----------------------------------------------------------
    # Sortie  : float, ex: 179.98 pour "Total : 179,98 €"
    # Indice  : l'élément a l'id "cart-total"
    #           pense à convertir la virgule en point avant float()
    # ----------------------------------------------------------
    def get_total(self) -> float:
        text = self.page.locator("#cart-total").inner_text()
        return float(text.replace("Total :", "").replace(" €", "").replace(",", "."))
