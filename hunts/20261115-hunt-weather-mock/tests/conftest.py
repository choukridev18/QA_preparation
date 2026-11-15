import pytest
from unittest import mock


@pytest.fixture
def mock_http_200():
    """Réponse HTTP 200 prête à brancher sur mock_get.return_value."""
    response = mock.Mock()
    response.status_code = 200
    return response
