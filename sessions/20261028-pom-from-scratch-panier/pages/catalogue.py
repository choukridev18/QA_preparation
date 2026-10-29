from playwright.sync_api import Page


class CataloguePage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        """ouvrir la page"""
        self.page.goto(self.URL)

    def add_to_basket(self, produit: str) -> None:
        """ajouter un produit au panier"""
        line = self.page.locator("#product-list li").filter(has_text=produit)
        line.get_by_role("button", name="Ajouter au panier").click()

    def get_count_badge(self) -> int:
        """retourne le nombre de produit dans le panier"""
        return int(self.page.locator("#cart-badge").inner_text())

    def get_count_products(self) -> int:
        """nombre de produits affichés sur le catalogue"""
        return self.page.locator("#product-list li").count()

    def go_to_cart(self) -> None:
        """ " Acceder au panier"""
        self.page.get_by_role("link", name="Panier").click()

    def empty_the_cart(self) -> None:
        """vider le panier"""
        self.page.get_by_role("button", name="Vider le panier").click()

    def return_to_main_page(self) -> None:
        """retourner dans la page principal"""
        self.page.get_by_role("link", name="Retour catalogue").click()

    def get_list_products_added(self) -> list[str]:
        """montre la liste des produits ajoutés"""
        return self.page.locator("#cart-lines li .line-name").all_inner_texts()

    def get_product_price(self, produit: str) -> str:
        """prix affiché pour un produit sur le catalogue"""
        return (
            self.page.locator("#product-list li")
            .filter(has_text=produit)
            .locator(".product-price")
            .inner_text()
        )

    def get_total_price(self) -> str:
        """montre le total du prix"""
        return self.page.locator("#cart-total").inner_text()

    def convert_price_product_in_float(self, produit: str) -> float:
        """convertit le prix d'un produit en décimale"""
        article = self.page.locator("#product-list li").filter(has_text=produit)
        text_prix = article.locator(".product-price").inner_text().split(" ")[0]
        convert = text_prix.split(" ")[0]
        return float(convert)
