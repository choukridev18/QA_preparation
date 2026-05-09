
from playwright.sync_api import Page


class TodosPage:
    """
    Page Object pour la page principale du gestionnaire de tâches.
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
    # TODO 2 — Ajouter une tâche
    # ----------------------------------------------------------
    # Entrée  : title="Faire les courses"
    # Attendu : formulaire soumis, tâche apparaît dans la liste
    # Indice  : l'input a un aria-label "Nouvelle tâche"
    # ----------------------------------------------------------
    def add_todo(self, title: str) -> None:
        self.page.get_by_label("Nouvelle tâche").fill(title)
        self.page.get_by_role("button",name="Ajouter").click()
        

    # ----------------------------------------------------------
    # TODO 3 — Marquer une tâche comme terminée
    # ----------------------------------------------------------
    # Entrée  : title="Faire les courses"
    # Attendu : bouton "Terminer" cliqué pour cette tâche
    # Indice  : le bouton a un aria-label "Marquer {title} comme terminée"
    # ----------------------------------------------------------
    def mark_done(self, title: str) -> None:
        
        self.page.get_by_label(f"Marquer {title} comme terminée").click()
       

    # ----------------------------------------------------------
    # TODO 4 — Supprimer une tâche
    # ----------------------------------------------------------
    # Entrée  : title="Faire les courses"
    # Attendu : bouton "Supprimer" cliqué pour cette tâche
    # Indice  : le bouton a un aria-label "Supprimer {title}"
    # ----------------------------------------------------------
    def delete_todo(self, title: str) -> None:
        self.page.get_by_label(f"Supprimer {title}").click()

    # ----------------------------------------------------------
    # TODO 5 — Appliquer un filtre
    # ----------------------------------------------------------
    # Entrée  : filtre="active" | "done" | "all"
    # Attendu : clic sur le lien de filtre correspondant
    # Indice  : les liens ont les textes "Actives", "Terminées", "Toutes"
    # ----------------------------------------------------------
    def set_filter(self, filtre: str) -> None:
        labels = {"all":"Toutes","active":"Actives","done":"Terminées"}
        self.page.get_by_role("link",name=labels[filtre]).click()

    # ----------------------------------------------------------
    # TODO 6 — Compter les tâches visibles dans la liste
    # ----------------------------------------------------------
    # Sortie  : entier — nombre de <li> dans #todo-list
    # ----------------------------------------------------------
    def get_visible_count(self) -> int:
        return self.page.locator("#todo-list li").count()

    # ----------------------------------------------------------
    # TODO 7 — Vérifier si le message "aucune tâche" est affiché
    # ----------------------------------------------------------
    # Sortie  : True si #empty-message est visible, False sinon
    # ----------------------------------------------------------
    def is_empty(self) -> bool:
        return self.page.locator("#empty-message").is_visible()
         
