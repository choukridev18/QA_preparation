import pytest
from src.notifications import create_notification


@pytest.fixture
def sample_notification():
    notif = create_notification("user123", "Serveur en surcharge", 0.8, 0.9)
    return notif
    # BUG: return manquant — la fixture retourne None
