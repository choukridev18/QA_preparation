import pytest
import src.booking as booking


@pytest.fixture(autouse=True)
def reset_bookings():
    """Remet l'état des réservations à zéro avant et après chaque test."""
    booking.BOOKINGS.clear()
    booking._next_id = 1
    yield
    booking.BOOKINGS.clear()
    booking._next_id = 1
