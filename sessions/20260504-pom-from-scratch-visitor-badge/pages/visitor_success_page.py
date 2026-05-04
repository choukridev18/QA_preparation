from playwright.sync_api import Page

class VisitorSuccessPage:
    """Écran final : numéro de dossier BADGE-… et lien pour refaire une demande."""

    PATH="/visitor/success"

    def __init__(self, page: Page, base_url:str):
        self.page = page
        self._base = base_url.rstrip("/")
    
    @property
    def url(self)->str:
        return f"{self._base}{self.PATH}"

    def navigate(self)->None:
        self.page.goto(self.url)
    
    def badge_id_text(self)-> str:
        return self.page.locator("#badge-id").inner_text()
    
    def click_new_request(self)-> None:
        self.page.get_by_role("link",name="Nouvelle demande").click()



