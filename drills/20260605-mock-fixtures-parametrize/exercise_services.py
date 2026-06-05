def send_email_api(to: str, subject: str, body: str) -> bool:
    """Real email API call — mocked in tests."""
    raise RuntimeError("Real email API — use mock in tests")


def send_sms_api(phone: str, message: str) -> bool:
    """Real SMS API call — mocked in tests."""
    raise RuntimeError("Real SMS API — use mock in tests")
