from playwright.sync_api import Page


class VisitorStep1Page:
    """Premier écran : nom, email, entreprise."""
    PATH = "/visitor/step1"

    def __init__(self,page: Page, base_url: str):
        self.page = page
        self._base = base_url.rstrip("/")

    @property
    def url(self) -> str:
        return f"{self._base}{self.PATH}"

    def navigate(self) -> None:
        self.page.goto(self.url)
    
    def fill_full_name(self, value:str)-> None:
        self.page.get_by_label("Nom complet").fill(value)

    def fill_email(self, value: str)-> None:
        self.page.get_by_label("Email professionnel").fill(value)
    
    def fill_company(self , value:str)-> None:
        self.page.get_by_label("Entreprise").fill(value)
    
    def click_next(self) -> None:
        self.page.get_by_role("button",name="Suivant").click()
