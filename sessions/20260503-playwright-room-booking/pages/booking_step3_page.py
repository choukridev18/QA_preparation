from playwright.sync_api import Page


class BookingStep3Page:
    """
    Page Object pour l'étape 3 — récapitulatif et confirmation.
    URL : http://localhost:5001/booking/step3
    """

    URL = "http://localhost:5001/booking/step3"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer directement vers cette URL (tests de garde-fou)
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Lire la date affichée dans le récapitulatif
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    def get_recap_date_text(self) -> str:
        return self.page.locator("#recap-date").inner_text()

    # ----------------------------------------------------------
    # TODO 3 — Lire le nom de salle affiché dans le récapitulatif
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    def get_recap_room_text(self) -> str:
        return self.page.locator("#recap-room").inner_text()

    # ----------------------------------------------------------
    # TODO 4 — Confirmer la réservation (POST vers la même page)
    # ----------------------------------------------------------
    #
    # ----------------------------------------------------------
    def confirm_booking(self) -> None:
        self.page.get_by_role("button", name="Confirmer la réservation").click()
