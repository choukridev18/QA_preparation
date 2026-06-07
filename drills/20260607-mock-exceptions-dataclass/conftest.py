import pytest
from exercise import Notification


@pytest.fixture
def notif():
    """Une notification simple pour les tests."""
    return Notification(
        recipient="alice@example.com",
        subject="Bienvenue",
        body="Bonjour Alice, bienvenue sur la plateforme.",
    )


@pytest.fixture
def notif_list():
    """Une liste de 3 notifications pour tester send_all."""
    return [
        Notification("alice@example.com", "Sujet A", "Corps A"),
        Notification("bob@example.com", "Sujet B", "Corps B"),
        Notification("charlie@example.com", "Sujet C", "Corps C"),
    ]
