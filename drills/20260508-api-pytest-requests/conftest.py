import pytest
import server as srv
from server import app


@pytest.fixture(autouse=True)
def reset_state():
    """Remet l'état de l'API à zéro avant chaque test."""
    srv.tasks.clear()
    srv.next_id = 1
    yield


@pytest.fixture
def client():
    """Client de test Flask — simule des requêtes HTTP sans lancer de serveur."""
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
