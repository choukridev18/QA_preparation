
from playwright.sync_api import Page

class VisitorStep3Page:
    """Écran 3 — récapitulatif et confirmation."""

    PATH= "/visitor/step3"

    def __init__(self,page: Page, base_url:str):
        self.page= page
        self._base = base_url.rstrip("/")

    @property
    def url(self) -> str:
        return {self._base} + {self.PATH}
    
    def navigate(self) -> None:
        self.page.goto(self.url)
    
    def recap_name(self) -> str:
        return self.page.locator("#recap-name").inner_text()
    
    def recap_email(self) -> str:
        return self.page.locator("#recap-email").inner_text()

    def recap_company(self) -> str:
        return self.page.locator("#recap-company").inner_text()

    def recap_visit_date(self) -> str:
        return self.page.locator("#recap-visit-date").inner_text()
    
    def recap_purpose(self) -> str:
        return self.page.locator("#recap-purpose").inner_text()
    
    def click_confirm(self) -> None:
        self.page.get_by_role("button",name= "Confirmer la demande").click()
    
    

    
    
