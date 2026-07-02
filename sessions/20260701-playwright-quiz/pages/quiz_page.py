from playwright.sync_api import Page


class QuizPage:
    """
    Page Object pour les pages de questions du quiz.
    URL : http://127.0.0.1:5001/quiz/1  (puis /quiz/2, /quiz/3)
    """

    BASE_URL = "http://127.0.0.1:5001"
    START_URL = "http://127.0.0.1:5001/quiz/1"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la première question
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.BASE_URL)

    # ----------------------------------------------------------
    # TODO 2 — Lire le numéro de question affiché
    # ----------------------------------------------------------
    # Sortie  : "Question 1 sur 3"
    # ----------------------------------------------------------
    def get_question_number(self) -> str:
        return self.page.locator("#question-number").inner_text()

    # ----------------------------------------------------------
    # TODO 3 — Lire le texte de la question
    # ----------------------------------------------------------
    # Sortie  : "Quelle est la capitale de la France ?"
    # ----------------------------------------------------------
    def get_question_text(self) -> str:
        return self.page.locator("#question-text").inner_text()

    # ----------------------------------------------------------
    # TODO 4 — Sélectionner une réponse par son texte
    # ----------------------------------------------------------
    # Entrée  : "Paris"
    # Attendu : le bouton radio associé est coché
    # ----------------------------------------------------------
    def select_answer(self, label: str) -> None:
        self.page.get_by_label(label).check()

    # ----------------------------------------------------------
    # TODO 5 — Cliquer sur le bouton de soumission
    # ----------------------------------------------------------
    # Selon la question : "Suivant" ou "Voir le score"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button").click()


class ResultPage:
    """
    Page Object pour la page de résultat.
    URL : http://127.0.0.1:5001/quiz/result
    """

    URL = "http://127.0.0.1:5001/quiz/result"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 6 — Lire le texte du score
    # ----------------------------------------------------------
    # Sortie  : "Votre score : 3/3"
    # ----------------------------------------------------------
    def get_score_text(self) -> str:
        return self.page.locator("#score").inner_text()

    # ----------------------------------------------------------
    # TODO 7 — Cliquer sur "Recommencer"
    # ----------------------------------------------------------
    # Attendu : retour à la question 1
    # ----------------------------------------------------------
    def restart(self) -> None:
        self.page.get_by_role("link", name="Recommencer").click()
