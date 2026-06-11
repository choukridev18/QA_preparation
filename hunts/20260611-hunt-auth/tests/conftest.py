import pytest
from src import auth


@pytest.fixture(scope="session")
def registered_user():
    """Crée un utilisateur de test et remet l'état à zéro après."""
    auth.reset()
    auth.register("alice", "secret123")
    yield {"username": "alice", "password": "secret123"}
    auth.reset()


@pytest.fixture
def active_token(registered_user):
    """Retourne un token valide pour alice."""
    token = auth.login(registered_user["username"], registered_user["password"])
    yield token
    auth.logout(token)
