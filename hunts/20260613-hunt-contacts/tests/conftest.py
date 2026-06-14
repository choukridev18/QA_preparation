import pytest
from src import contacts


@pytest.fixture(autouse=True)
def reset_contacts():
    contacts.reset()
    yield
    contacts.reset()


@pytest.fixture
def populated():
    """Carnet avec 3 contacts pré-ajoutés."""
    contacts.add_contact("Zineb Amrani", "zineb@example.com", "0601020304")
    contacts.add_contact("Alice Dupont", "alice@example.com")
    contacts.add_contact("Marc Bernard", "marc@example.com", "0698765432")
