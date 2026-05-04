from playwright.sync_api import Page, expect
from pages.visitor_step1_page import VisitorStep1Page
from pages.visitor_step2_page import VisitorStep2Page
from pages.visitor_step3_page import VisitorStep3Page
from pages.visitor_success_page import VisitorSuccessPage

def test_full_visitor_flow_shows_badge_id(page: Page, app_url: str) -> None:
    """Parcours étapes 1→2→3 puis succès ; le dossier commence par BADGE-."""
    s1 = VisitorStep1Page(page, app_url)
    s1.navigate()
    s1.fill_full_name("Jean Test")
    s1.fill_email("jean@example.com")
    s1.fill_company("ACME")
    s1.click_next()
    expect(page).to_have_url(f"{app_url.rstrip('/')}/visitor/step2")

    s2 = VisitorStep2Page(page,app_url)
    s2.fill_visit_date("2030-06-15")
    s2.select_purpose("Réunion client")
    s2.click_next()
    expect(page).to_have_url(f"{app_url.rstrip('/')}/visitor/step3")

    s3 = VisitorStep3Page(page, app_url)
    assert s3.recap_name().strip() == "Jean Test"
    s3.click_confirm()
    expect(page).to_have_url(f"{app_url.rstrip('/')}/visitor/success")
    success = VisitorSuccessPage(page, app_url)
    assert success.badge_id_text().strip().startswith("BADGE-")

def test_open_step2_without_session_redirects_to_step1(page: Page, app_url: str) -> None:
    s2 = VisitorStep2Page(page, app_url)
    s2.navigate()
    expect(page).to_have_url(f"{app_url.rstrip('/')}/visitor/step1")
    
def test_open_success_without_badge_redirects_to_step1(page: Page, app_url: str) -> None:
    out = VisitorSuccessPage(page, app_url)
    out.navigate()
    expect(page).to_have_url(f"{app_url.rstrip('/')}/visitor/step1")