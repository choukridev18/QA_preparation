"""
Module de gestion de tâches (todos).
"""


TODOS: list[dict] = []
_next_id: int = 1


def add_todo(title: str, priority: str = "normale") -> dict:
    """
    Ajoute une tâche et retourne le dict créé.
    Format : {"id": int, "title": str, "priority": str, "done": False}
    priority accepte : "haute", "normale", "basse"
    Lève ValueError si priority n'est pas valide.
    """
    global _next_id
    valid_priorities = ["haute", "normale", "basse"]
    if priority not in valid_priorities:
        raise ValueError(f"Priorité invalide : {priority!r}")
    todo = {"id": _next_id, "title": title, "priority": priority, "done": False}
    TODOS.append(todo)
    _next_id += 1
    return todo


def complete_todo(todo_id: int) -> bool:
    """
    Marque une tâche comme faite.
    Retourne True si trouvée et mise à jour, False sinon.
    """
    for todo in TODOS:
        if todo["id"] == todo_id:
            todo["done"] = True
            return True
    return False


def get_pending(todos: list[dict]) -> list[dict]:
    """
    Retourne les tâches non faites (done=False), triées par id croissant.
    """
    return sorted([t for t in todos if not t["done"]], key=lambda t: t["id"])


def format_title(title: str) -> str:
    """
    Retourne le titre avec la première lettre en majuscule et le reste en minuscule.
    Exemple : "FAIRE LA VAISSELLE" → "Faire la vaisselle"
    """
    return title.capitalize()
