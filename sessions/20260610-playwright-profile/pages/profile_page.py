from playwright.sync_api import Page


class ProfilePage:
    """
    Page Object pour la page de consultation du profil.
    URL : http://localhost:5001/profile
    """

    URL = "http://localhost:5001/profile"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 1 — Naviguer vers la page profil
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 2 — Cliquer sur le lien "Modifier le profil"
    # ----------------------------------------------------------
    # Attendu : l'URL devient http://localhost:5001/profile/edit
    # ----------------------------------------------------------
    def go_to_edit(self) -> None:
        self.page.get_by_role("link", name="Modifier le profil").click()

    # ----------------------------------------------------------
    # TODO 3 — Lire le nom affiché sur la page profil
    # ----------------------------------------------------------
    # Sortie : ex. "Alice Martin"
    # ----------------------------------------------------------
    def get_name(self) -> str:
        return self.page.locator("#profile-name").inner_text()

    # ----------------------------------------------------------
    # TODO 4 — Lire l'email affiché sur la page profil
    # ----------------------------------------------------------
    # Sortie : ex. "alice@example.com"
    # ----------------------------------------------------------
    def get_email(self) -> str:
        return self.page.locator("#profile-email").inner_text()

    # ----------------------------------------------------------
    # TODO 5 — Vérifier si le message de succès est visible
    # ----------------------------------------------------------
    # Sortie : True si "#success-message" est présent dans la page
    # ----------------------------------------------------------
    def has_success_message(self) -> bool:
        return self.page.locator("#success-message").count() > 0


class EditProfilePage:
    """
    Page Object pour le formulaire de modification du profil.
    URL : http://localhost:5001/profile/edit
    """

    URL = "http://localhost:5001/profile/edit"

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------------------------------------
    # TODO 6 — Naviguer vers le formulaire d'édition
    # ----------------------------------------------------------
    def navigate(self) -> None:
        self.page.goto(self.URL)

    # ----------------------------------------------------------
    # TODO 7 — Remplir le champ "Nom"
    # ----------------------------------------------------------
    # Entrée  : name="Bob Dupont"
    # Attendu : le champ "Nom" contient "Bob Dupont"
    # ----------------------------------------------------------
    def fill_name(self, name: str) -> None:
        self.page.get_by_label("Nom").fill(name)

    # ----------------------------------------------------------
    # TODO 8 — Remplir le champ "Email"
    # ----------------------------------------------------------
    # Entrée  : email="bob@example.com"
    # ----------------------------------------------------------
    def fill_email(self, email: str) -> None:
        self.page.get_by_label("Email").fill(email)

    # ----------------------------------------------------------
    # TODO 9 — Remplir le champ "Bio"
    # ----------------------------------------------------------
    # Entrée  : bio="Testeur QA junior."
    # ----------------------------------------------------------
    def fill_bio(self, bio: str) -> None:
        self.page.get_by_label("Bio").fill(bio)

    # ----------------------------------------------------------
    # TODO 10 — Soumettre le formulaire
    # ----------------------------------------------------------
    # Attendu : clic sur le bouton "Enregistrer"
    # ----------------------------------------------------------
    def submit(self) -> None:
        self.page.get_by_role("button", name="Enregistrer").click()

    # ----------------------------------------------------------
    # TODO 11 — Lire le message d'erreur du champ "Nom"
    # ----------------------------------------------------------
    # Sortie  : ex. "Le nom est requis." — chaîne vide si pas d'erreur
    # ----------------------------------------------------------
    def get_name_error(self) -> str:
        return self.page.locator("#error-name").inner_text()

    # ----------------------------------------------------------
    # TODO 12 — Lire le message d'erreur du champ "Email"
    # ----------------------------------------------------------
    # Sortie  : ex. "L'email n'est pas valide." — chaîne vide si pas d'erreur
    # ----------------------------------------------------------
    def get_email_error(self) -> str:
        return self.page.locator("#error-email").inner_text()

    def click_cancel(self) -> None:
        self.page.get_by_role("link", name="Annuler").click()
