from playwright.sync_api import Page

class VisitorStep2Page:
    """Écran 2 — date et motif de visite."""

    PATH = "/visitor/step2"

    def __init__(self,page :Page, base_url :str):
        self.page = page
        self._base= base_url.rstrip("/")

    @property
    def url(self)-> str:
        return f"{self._base}{self.PATH}"

    def navigate(self)-> None:
        self.page.goto(self.url)
    
    def fill_visit_date(self, iso_date:str) ->None:
        self.page.get_by_label("Date de visite").fill(iso_date)
    
    def select_purpose(self,option_label:str)-> None:
        self.page.get_by_label("Motif de la visite").select_option(label=option_label)
    
    def click_next(self)-> None:
        self.page.get_by_role("button",name="Suivant").click()
