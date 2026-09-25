import pytest

from exercise import EmailMessage


@pytest.fixture
def welcome_message():
    """Message de bienvenue typique d'une app SaaS."""
    return EmailMessage(
        to="new.user@saas.io",
        subject="Bienvenue",
        body="Votre compte est prêt.",
    )


@pytest.fixture
def api_ok_response():
    return {"id": "msg-42", "status": "ok"}
