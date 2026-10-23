from playwright.sync_api import Page


class DashboardPage:

    URL = "http://127.0.0.1:5001"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def get_total_deliveries(self) -> int:
        text = self.page.locator("#count-tous").inner_text()
        return int(text.split(":")[1].strip())

    def filter_by(self, statut: str) -> None:
        self.page.get_by_role("link", name=statut).click()

    def get_count_en_cours(self) -> int:
        text = self.page.locator("#count-en-cours").inner_text()
        return int(text.split(":")[1].strip())

    def update_status(self, livraison_id: int, nouveau_statut: str) -> None:

        row = self.page.locator(f"#livraison-{livraison_id}")
        row.get_by_label("Nouveau statut").select_option(nouveau_statut)
        row.get_by_role(
            "button", name=f"Mettre à jour livraison {livraison_id}"
        ).click()

    def get_status(self, livraison_id: int) -> str:
        return self.page.locator(f"#statut-{livraison_id}").inner_text()

    def get_row_count(self) -> int:
        return self.page.get_by_role("row").count() - 1
