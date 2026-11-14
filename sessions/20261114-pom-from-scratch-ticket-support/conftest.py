import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(autouse=True)
def reset_data():
    requests.post(f"{BASE_URL}/reset")
    yield
    requests.post(f"{BASE_URL}/reset")
