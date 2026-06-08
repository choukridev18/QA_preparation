import pytest
import src.todos as todos


# -------------------------------------------------------
# Tests qui passent
# -------------------------------------------------------


def test_add_todo_returns_dict(reset_todos):
    """add_todo retourne un dict avec les bons champs."""
    result = todos.add_todo("Faire les courses")
    assert result["title"] == "Faire les courses"
    assert result["done"] is False
    assert result["priority"] == "normale"


def test_complete_todo_returns_true(reset_todos):
    """complete_todo retourne True quand la tâche existe."""
    t = todos.add_todo("Tâche test")
    assert todos.complete_todo(t["id"]) is True


def test_complete_todo_returns_false_if_not_found(reset_todos):
    """complete_todo retourne False si l'id n'existe pas."""
    assert todos.complete_todo(999) is False


# -------------------------------------------------------
# Tests avec bugs — à corriger uniquement dans ce fichier
# -------------------------------------------------------


def test_format_title_capitalizes(reset_todos):
    """format_title met la première lettre en majuscule, le reste en minuscule."""
    assert todos.format_title("FAIRE LA VAISSELLE") == "Faire la vaisselle"


def test_add_todo_raises_on_invalid_priority(reset_todos):
    """add_todo lève une erreur si la priorité est invalide."""
    with pytest.raises(ValueError):
        todos.add_todo("Tâche", priority="urgente")


def test_get_pending_returns_only_undone(sample_todos):
    """get_pending retourne uniquement les tâches non faites."""
    result = todos.get_pending(sample_todos)
    assert len(result) == 2
    titles = [t["title"] for t in result]
    assert titles == [
        "Faire les courses",
        "Appeler le médecin",
    ]


def test_add_todo_increments_id(reset_todos):
    """Les ids sont incrémentaux à partir de 1."""
    t1 = todos.add_todo("Tâche 1")
    t2 = todos.add_todo("Tâche 2")
    assert t2["id"] == t1["id"] + 1
    assert t1["id"] == 1
