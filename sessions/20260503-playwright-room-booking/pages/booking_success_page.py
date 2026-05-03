from playwright.sync_api import Page


class BookingSuccessPage:
    """
    Page Object pour la page de confirmation finale.
    URL : http://localhost:5001/booking/success
    """

    URL = "http://localhost:5001/booking/success"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Lire la référence de réservation affichée
    # ----------------------------------------------------------
    # Sortie  : texte du strong#booking-reference (ex. "BK-A1B2C3")
    #
    # ----------------------------------------------------------
    def get_booking_reference(self) -> str:
        return self.page.locator("#booking-reference").inner_text()
