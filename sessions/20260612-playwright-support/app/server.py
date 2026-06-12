from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CATEGORIES = ["Bug", "Question", "Amélioration"]

DEFAULT_TICKETS = [
    {"id": 1, "title": "Login ne fonctionne pas", "category": "Bug", "status": "Ouvert"},
    {"id": 2, "title": "Comment changer mon email ?", "category": "Question", "status": "Ouvert"},
]

TICKETS: list[dict] = []
_next_id: int = 1


def _reset_tickets():
    global TICKETS, _next_id
    TICKETS = [dict(t) for t in DEFAULT_TICKETS]
    _next_id = len(DEFAULT_TICKETS) + 1


_reset_tickets()


@app.route("/reset", methods=["POST"])
def reset():
    _reset_tickets()
    return "", 204


@app.route("/")
def index():
    return redirect(url_for("ticket_list"))


@app.route("/tickets", methods=["GET"])
def ticket_list():
    open_count = sum(1 for t in TICKETS if t["status"] == "Ouvert")
    return render_template("tickets.html", tickets=TICKETS, open_count=open_count)


@app.route("/tickets/new", methods=["GET"])
def ticket_new():
    return render_template("new_ticket.html", categories=CATEGORIES, errors={}, form={})


@app.route("/tickets/new", methods=["POST"])
def ticket_new_post():
    global _next_id
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()

    errors = {}
    if not title:
        errors["title"] = "Le titre est requis."
    if not category or category not in CATEGORIES:
        errors["category"] = "Choisissez une catégorie valide."

    if errors:
        form = {"title": title, "category": category, "description": description}
        return render_template("new_ticket.html", categories=CATEGORIES, errors=errors, form=form), 422

    TICKETS.append({
        "id": _next_id,
        "title": title,
        "category": category,
        "status": "Ouvert",
    })
    _next_id += 1
    return redirect(url_for("ticket_list"))


@app.route("/tickets/<int:ticket_id>/resolve", methods=["POST"])
def ticket_resolve(ticket_id):
    for ticket in TICKETS:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Résolu"
            break
    return redirect(url_for("ticket_list"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
