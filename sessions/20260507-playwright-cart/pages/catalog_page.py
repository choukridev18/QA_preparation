from playwright.sync_api import Page


class CatalogPage:
    """
    Page Object pour le catalogue de produits.
    URL : http://localhost:5001/
    """

    URL = "http://localhost:5001/"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page catalogue
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Ajouter un produit au panier
    # ----------------------------------------------------------
    # Entrée  : product_name="Clavier mécanique", quantity=2
    # Attendu : formulaire soumis → redirection vers le catalogue
    # Indice  : l'input quantité a un aria-label "Quantité pour {product_name}"
    # ----------------------------------------------------------
    def add_to_cart(self, product_name: str, quantity: int = 1) -> None:
        self.page.get_by_label(f"Quantité pour {product_name}").fill(str(quantity))
        self.page.locator("article").filter(has_text= product_name).get_by_role("button",name="Ajouter au panier").click()

    # ----------------------------------------------------------
    # TODO 3 — Naviguer vers le panier via le lien dans la nav
    # ----------------------------------------------------------
    # Attendu : page naviguée vers /cart
    # Indice  : le lien commence par "Panier"
    # ----------------------------------------------------------
    def go_to_cart(self) -> None:
        self.page.get_by_role("link",name="Panier",exact=False).click()
        

    # ----------------------------------------------------------
    # TODO 4 — Lire le compteur d'articles dans la nav
    # ----------------------------------------------------------
    # Sortie  : entier, ex: 2 si "Panier (2)" affiché dans la nav
    # Indice  : l'élément a l'id "cart-link"
    # ----------------------------------------------------------
    def get_cart_count(self) -> int:
        text = self.page.locator("#cart-link").inner_text()
        return int(text.split("(")[1].rstrip(")"))
