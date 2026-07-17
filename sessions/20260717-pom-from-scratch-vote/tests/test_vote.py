from playwright.sync_api import Page, expect
import pytest
from pages.vote_page import Vote, Results


def test_vote_valide_redirect_to_page_results(page: Page):
    """Effectuer un vote valide redirige vers la page 'results'"""
    v = Vote(page)
    v.navigate()
    v.choice_langage("Go")
    v.submit_vote()
    expect(page).to_have_url(Results.URL)


def test_get_message_error_if_vote_two_times(page: Page):
    """Un message 'Vous avez déjà voté.' apparait si on vote 2 fois"""
    v = Vote(page)
    v.navigate()
    v.choice_langage("Go")
    v.submit_vote()
    v.navigate()
    v.choice_langage("Go")
    v.submit_vote()
    assert v.get_error_message() == "Vous avez déjà voté."


def test_get_message_error_if_submit_without_option(page: Page):
    """Un message d'erreur s'affiche si on vote sans choisir d'option"""
    v = Vote(page)
    v.navigate()
    v.submit_vote()
    assert v.get_error_message() == "Veuillez sélectionner une option avant de voter."


def test_get_correct_results_vote(page: Page):
    """Les bons résultats des votes s'affichent correctement."""
    v = Vote(page)
    v.navigate()
    v.choice_langage("Go")
    v.submit_vote()
    r = Results(page)
    assert "1" in r.get_total_vote()
    r.click_vote_again()
    v.choice_langage("Java")
    v.submit_vote()
    assert "2" in r.get_total_vote()


def test_link_new_vote_redirect_to_main_page(page: Page):
    """Le lien 'Voter à nouveau redirige vers la page vote"""
    v = Vote(page)
    v.navigate()
    v.choice_langage("Go")
    v.submit_vote()
    r = Results(page)
    r.click_vote_again()
    expect(page).to_have_url(Vote.URL)
