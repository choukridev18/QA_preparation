import pytest
from unittest import mock
import src.booking as booking


# ---------------------------------------------------------------------------
# Tests qui passent
# ---------------------------------------------------------------------------


def test_book_slot_creates_booking_id():
    """book_slot retourne un identifiant au format BOOKING-XXXX."""
    booking_id = booking.book_slot(slot_id=42, user_email="alice@example.com")
    assert booking_id.startswith("BOOKING-")
    assert len(booking_id) == 12


def test_calculate_price_no_discount():
    """Sans remise, calculate_price retourne le prix de base inchangé."""
    result = booking.calculate_price(100.0, 0.0)
    assert result == 100.0


def test_cancel_booking_returns_true():
    """cancel_booking retourne True quand la réservation existe."""
    booking_id = booking.book_slot(slot_id=1, user_email="bob@example.com")
    result = booking.cancel_booking(booking_id)
    assert result is True


# ---------------------------------------------------------------------------
# Tests avec bugs — à corriger uniquement dans ce fichier
# ---------------------------------------------------------------------------


@mock.patch("src.booking.requests.get")
def test_get_available_slots_returns_list(mock_get):
    """get_available_slots retourne la liste des créneaux de l'API."""
    mock_get.return_value.json.return_value = {"slots": [{"id": 1}, {"id": 2}]}
    mock_get.return_value.raise_for_status.return_value = None

    result = booking.get_available_slots("2026-06-10")

    assert len(result) == 2
    mock_get.assert_called_once()


@mock.patch("src.booking.requests.post")
def test_send_confirmation_email_success(mock_post):
    """send_confirmation_email retourne True quand le serveur répond 200."""
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    result = booking.send_confirmation_email("alice@example.com", "BOOKING-0001")

    assert result is True


def test_cancel_nonexistent_booking_raises():
    """cancel_booking lève une exception si la réservation n'existe pas."""
    with pytest.raises(ValueError):
        booking.cancel_booking("BOOKING-9999")


def test_calculate_price_with_discount():
    """calculate_price applique correctement une remise de 70%."""
    result = booking.calculate_price(1.0, 0.7)
    assert result == pytest.approx(0.3)
