from playwright.sync_api import Page


class BookingStep1Page:
    """
    Page Object pour l'étape 1 — date et choix de salle.
    URL : http://localhost:5001/booking/step1
    """

    URL = "http://localhost:5001/booking/step1"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Renseigner la date (format ISO AAAA-MM-JJ)
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    def fill_booking_date(self, iso_date: str) -> None:
        self.page.get_by_label("Date de la réservation").fill(iso_date)

    # ----------------------------------------------------------
    # TODO 3 — Choisir une salle dans la liste déroulante
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    def select_room(self, room_label: str) -> None:
        self.page.get_by_label("Salle").select_option(label=room_label)

    # ----------------------------------------------------------
    # TODO 4 — Passer à l'étape suivante
    # ----------------------------------------------------------
    def click_next(self) -> None:
        self.page.get_by_role("button", name="Suivant").click()
