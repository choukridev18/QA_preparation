from playwright.sync_api import Page


class NotesListPage:
    """
    Page Object pour la liste des notes.
    URL : http://localhost:5001/
    """

    URL = "http://localhost:5001/"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Aller vers la page de création de note
    # ----------------------------------------------------------
    # Attendu : le navigateur charge /new
    # ----------------------------------------------------------
    def go_to_new_note(self) -> None:
        self.page.get_by_role("link", name="Nouvelle note").click()

    # ----------------------------------------------------------
    # TODO 3 — Lire le nombre de notes affichées
    # ----------------------------------------------------------
    # Sortie  : 2  (si "2 note(s)" est affiché)
    # ----------------------------------------------------------
    def get_note_count(self) -> int:
        return int(self.page.locator("#note-count").inner_text().split()[0])

    # ----------------------------------------------------------
    # TODO 4 — Lire les titres de toutes les notes
    # ----------------------------------------------------------
    # Sortie  : ["Réunion équipe", "Idées projet"]
    # ----------------------------------------------------------
    def get_note_titles(self) -> list[str]:
        return self.page.locator(".note-title").all_inner_texts()

    # ----------------------------------------------------------
    # TODO 5 — Cliquer sur "Modifier" pour une note donnée
    # ----------------------------------------------------------
    # Entrée  : note_id = 1
    # Attendu : le navigateur charge /edit/1
    # ----------------------------------------------------------
    def edit_note(self, note_id: int) -> None:
        self.page.get_by_role("link", name=f"Modifier la note {note_id}").click()

    # ----------------------------------------------------------
    # TODO 6 — Cliquer sur "Supprimer" pour une note donnée
    # ----------------------------------------------------------
    # Entrée  : note_id = 1
    # Attendu : la note disparaît de la liste
    # ----------------------------------------------------------
    def delete_note(self, note_id: int) -> None:
        self.page.get_by_role("button", name=f"Supprimer la note {note_id}").click()


class NewNotePage:
    """
    Page Object pour le formulaire de création de note.
    URL : http://localhost:5001/new
    """

    URL = "http://localhost:5001/new"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 7 — Naviguer vers la page
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 8 — Remplir le champ Titre
    # ----------------------------------------------------------
    def fill_title(self, value: str) -> None:
        self.page.get_by_label("Titre").fill(value)

    # ----------------------------------------------------------
    # TODO 9 — Remplir le champ Contenu
    # ----------------------------------------------------------
    def fill_content(self, value: str) -> None:
        self.page.get_by_label("Contenu").fill(value)

    # ----------------------------------------------------------
    # TODO 10 — Soumettre le formulaire
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Enregistrer").click()

    # ----------------------------------------------------------
    # TODO 11 — Lire le message d'erreur sur le titre
    # ----------------------------------------------------------
    # Sortie  : "Le titre est obligatoire."
    # ----------------------------------------------------------
    def get_title_error(self) -> str:
        return self.page.locator("#error-title").inner_text()

    # ----------------------------------------------------------
    # TODO 12 — Lire le message d'erreur sur le contenu
    # ----------------------------------------------------------
    # Sortie  : "Le contenu est obligatoire."
    # ----------------------------------------------------------
    def get_content_error(self) -> str:
        return self.page.locator("#error-content").inner_text()

    def cancel(self) -> None:
        self.page.get_by_role("link", name="Annuler").click()


class EditNotePage:
    """
    Page Object pour le formulaire d'édition de note.
    URL : http://localhost:5001/edit/<note_id>
    """

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 13 — Remplir le champ Titre (efface l'existant)
    # ----------------------------------------------------------
    def fill_title(self, value: str) -> None:
        self.page.get_by_label("Titre").fill(value)

    # ----------------------------------------------------------
    # TODO 14 — Remplir le champ Contenu (efface l'existant)
    # ----------------------------------------------------------
    def fill_content(self, value: str) -> None:
        self.page.get_by_label("Contenu").fill(value)

    # ----------------------------------------------------------
    # TODO 15 — Soumettre le formulaire
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Enregistrer").click()

    # ----------------------------------------------------------
    # TODO 16 — Lire le message d'erreur sur le titre
    # ----------------------------------------------------------
    # Sortie  : "Le titre est obligatoire."
    # ----------------------------------------------------------
    def get_title_error(self) -> str:
        return self.page.locator("#error-title").inner_text()
