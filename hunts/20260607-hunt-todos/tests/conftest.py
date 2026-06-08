import pytest
import src.todos as todos


@pytest.fixture
def reset_todos():
    """Remet la liste de tâches à zéro avant chaque test."""
    todos.TODOS.clear()
    todos._next_id = 1
    yield
    todos.TODOS.clear()
    todos._next_id = 1


@pytest.fixture
def sample_todos(reset_todos):
    """3 tâches pré-créées : 2 en cours, 1 faite."""
    todos.add_todo("Faire les courses", priority="haute")
    todos.add_todo("Appeler le médecin", priority="normale")
    t = todos.add_todo("Lire un livre", priority="basse")
    todos.complete_todo(t["id"])
    return todos.TODOS
