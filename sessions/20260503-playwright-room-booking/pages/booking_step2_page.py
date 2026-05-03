from playwright.sync_api import Page


class BookingStep2Page:
    """
    Page Object pour l'étape 2 — créneau et nombre de participants.
    URL : http://localhost:5001/booking/step2
    """

    URL = "http://localhost:5001/booking/step2"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer directement vers cette URL (tests de garde-fou)
    # ----------------------------------------------------------
    # Indice : self.page.goto(self.URL)
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Choisir le créneau
    # ----------------------------------------------------------
    # Entrée  : libellé exact d'une option, ex. "Matin (9h–12h)"
    # Indice  : get_by_label("Créneau").select_option(label=slot_label)
    # ----------------------------------------------------------
    def select_time_slot(self, slot_label: str) -> None:
        self.page.get_by_label("Créneau").select_option(label=slot_label)

    # ----------------------------------------------------------
    # TODO 3 — Indiquer le nombre de participants
    # ----------------------------------------------------------
    # Indice  : get_by_label("Nombre de participants").fill(str(n))
    # ----------------------------------------------------------
    def set_attendees(self, count: int) -> None:
        self.page.get_by_label("Nombre de participants").fill(str(count))
        

    # ----------------------------------------------------------
    # TODO 4 — Passer à l'étape suivante
    # ----------------------------------------------------------
    # Indice  : get_by_role("button", name="Suivant").click()
    # ----------------------------------------------------------
    def click_next(self) -> None:
        self.page.get_by_role("button",name="Suivant").click()
