import requests


def calculate_priority(urgency: float, impact: float) -> float:
    """Returns a priority score: urgency * impact."""
    return urgency * impact


def send_alert(recipient: str, message: str) -> bool:
    """Sends an alert via external API. Returns True on success."""
    response = requests.post(
        "https://api.alerts.internal/send",
        json={"to": recipient, "body": message},
    )
    return response.status_code == 200


def format_message(template: str, data: dict) -> str:
    """Formats a notification message using a template with placeholders."""
    return template.format(**data)


def get_priority_label(score: float) -> str:
    """Returns 'low', 'medium', or 'high' based on priority score."""
    if score < 2.0:
        return "low"
    elif score < 7.0:
        return "medium"
    else:
        return "high"


def create_notification(user_id: str, message: str, urgency: float, impact: float) -> dict:
    """Creates a notification dict for a given user.

    Raises ValueError if user_id is empty.
    """
    if not user_id:
        raise ValueError("user_id cannot be empty")
    score = calculate_priority(urgency, impact)
    return {
        "user_id": user_id,
        "message": message,
        "priority_score": score,
        "priority_label": get_priority_label(score),
    }
