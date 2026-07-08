from playwright.sync_api import Page


class OrdersPage:
    """
    Page Object pour le tableau de bord des commandes.
    URL : http://127.0.0.1:5001/
    """

    URL = "http://127.0.0.1:5001/"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers le tableau de bord
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Filtrer les commandes par statut
    # ----------------------------------------------------------
    # Entrée  : "en attente" / "expédiée" / "livrée" / "" (tous)
    # Attendu : la liste se met à jour avec le filtre appliqué
    # ----------------------------------------------------------
    def filter_by_status(self, status: str) -> None:
        self.page.locator("#filter-status").select_option(status)
        self.page.get_by_role("button", name="Filtrer").click()

    # ----------------------------------------------------------
    # TODO 3 — Lire le nombre de commandes affichées
    # ----------------------------------------------------------
    # Sortie  : 5 (si pas de filtre), 2 (si filtre "en attente")
    # ----------------------------------------------------------
    def get_order_count(self) -> int:
        return int(self.page.locator("#order-count").inner_text().split()[0])

    # ----------------------------------------------------------
    # TODO 4 — Changer le statut d'une commande
    # ----------------------------------------------------------
    # Entrée  : order_id=1, new_status="livrée"
    # Attendu : le statut de la commande 1 devient "livrée"
    # ----------------------------------------------------------
    def change_order_status(self, order_id: int, new_status: str) -> None:
        self.page.locator(f"#new-status-{order_id}").select_option(new_status)
        self.page.get_by_role(
            "button", name=f"Mettre à jour commande {order_id}"
        ).click()

    # ----------------------------------------------------------
    # TODO 5 — Lire le statut affiché d'une commande
    # ----------------------------------------------------------
    # Entrée  : order_id=1
    # Sortie  : "en attente"
    # ----------------------------------------------------------
    def get_order_status(self, order_id: int) -> str:
        return self.page.locator(f"#status-{order_id}").inner_text()

    # ----------------------------------------------------------
    # TODO 6 — Lire le compteur "En attente" dans les stats
    # ----------------------------------------------------------
    # Sortie  : 2
    # ----------------------------------------------------------
    def get_pending_count(self) -> int:
        return int(self.page.locator("#count-pending").inner_text())

    # ----------------------------------------------------------
    # TODO 7 — Lire le compteur "Livrées" dans les stats
    # ----------------------------------------------------------
    # Sortie  : 2
    # ----------------------------------------------------------
    def get_delivered_count(self) -> int:
        return int(self.page.locator("#count-delivered").inner_text())
