import pytest


@pytest.fixture
def with_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://localhost/testdb")
    yield
    # monkeypatch restaure automatiquement les variables après le test


@pytest.fixture
def with_debug_env(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://localhost/testdb")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    yield
