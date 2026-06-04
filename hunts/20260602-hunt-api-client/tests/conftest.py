import pytest
from unittest import mock


@pytest.fixture
def mock_success_response():
    response = mock.Mock()
    response.status_code = 200
    return response


@pytest.fixture
def mock_404_response():
    response = mock.Mock()
    response.status_code = 404
    return response
