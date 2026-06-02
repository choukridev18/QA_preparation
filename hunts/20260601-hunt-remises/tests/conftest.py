import pytest


@pytest.fixture
def sample_prices():
    return [15.0, 3.0, 8.5, 1.0, 22.0]


@pytest.fixture
def base_price():
    return 100.0
