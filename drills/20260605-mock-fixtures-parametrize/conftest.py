import pytest
from exercise import User


@pytest.fixture
def email_user():
    return User(name="Alice", email="alice@example.com", phone="+33600000001", channel="email")


@pytest.fixture
def sms_user():
    return User(name="Bob", email="bob@example.com", phone="+33600000002", channel="sms")
