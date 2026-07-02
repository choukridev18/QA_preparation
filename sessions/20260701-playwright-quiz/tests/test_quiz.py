import pytest
from playwright.sync_api import Page, expect
from pages.quiz_page import QuizPage, ResultPage


def test_first_question_is_displayed(page: Page):
    """Naviguer vers le quiz affiche bien la question 1"""
    q = QuizPage(page)
    q.navigate()

    assert "Question 1 sur 3" in q.get_question_number()
    assert "France" in q.get_question_text()


def test_complete_quiz_perfect_score(page: Page):
    """Répondre correctement à toutes les questions → score 3/3"""
    q = QuizPage(page)
    q.navigate()

    q.select_answer("Paris")
    q.submit()

    q.select_answer("56")
    q.submit()

    q.select_answer("Pacifique")
    q.submit()

    r = ResultPage(page)
    expect(page).to_have_url(ResultPage.URL)
    assert "3/3" in r.get_score_text()


def test_complete_quiz_zero_score(page: Page):
    """Répondre incorrectement à toutes les questions → score 0/3"""
    q = QuizPage(page)
    q.navigate()

    q.select_answer("Londres")
    q.submit()

    q.select_answer("54")
    q.submit()

    q.select_answer("Atlantique")
    q.submit()

    r = ResultPage(page)
    expect(page).to_have_url(ResultPage.URL)
    assert "0/3" in r.get_score_text()


def test_click_restart_redirect_question_1(page: Page):
    """Cliquer sur 'Recommencer' redirige vers la page 1"""
    p = QuizPage(page)
    p.navigate()
    p.select_answer("Paris")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/2")
    p.select_answer("56")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/3")
    p.select_answer("Pacifique")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/result")
    page_result = ResultPage(page)
    page_result.restart()
    expect(page).to_have_url(QuizPage.START_URL)


def test_result_shows_your_score_is_one_in_three(page: Page):
    """Le resultat 'votre score : 1/3' est affiché"""
    p = QuizPage(page)
    p.navigate()
    p.select_answer("Paris")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/2")
    p.select_answer("64")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/3")
    p.select_answer("Indien")
    p.submit()
    expect(page).to_have_url(f"{QuizPage.BASE_URL}/quiz/result")
    page_result = ResultPage(page)
    assert page_result.get_score_text() == "Votre score : 1/3"
