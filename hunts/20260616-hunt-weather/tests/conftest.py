import pytest


@pytest.fixture
def forecast_paris():
    return {"city": "Paris", "temp": 22.5, "condition": "Ensoleillé"}


@pytest.fixture
def forecast_hot():
    return {"city": "Séville", "temp": 38.0, "condition": "Très chaud"}
