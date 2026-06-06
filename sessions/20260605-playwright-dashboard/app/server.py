from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

TICKETS = [
    {"id": 1, "title": "Bug connexion impossible", "status": "ouvert", "priority": "haute"},
    {"id": 2, "title": "Export CSV ne fonctionne pas", "status": "ouvert", "priority": "basse"},
    {"id": 3, "title": "Lenteur page tableau de bord", "status": "en_cours", "priority": "haute"},
    {"id": 4, "title": "Email de confirmation manquant", "status": "en_cours", "priority": "basse"},
    {"id": 5, "title": "Erreur 500 sur facturation", "status": "ferme", "priority": "haute"},
    {"id": 6, "title": "Typo page d'accueil", "status": "ferme", "priority": "basse"},
]


def filter_tickets(status: str, priority: str, search: str) -> list:
    results = TICKETS
    if status:
        results = [t for t in results if t["status"] == status]
    if priority:
        results = [t for t in results if t["priority"] == priority]
    if search:
        search_lower = search.lower()
        results = [t for t in results if search_lower in t["title"].lower()]
    return results


@app.route("/")
def index():
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")
    search = request.args.get("search", "")
    tickets = filter_tickets(status, priority, search)
    return render_template(
        "dashboard.html",
        tickets=tickets,
        status=status,
        priority=priority,
        search=search,
    )


@app.route("/reset", methods=["POST"])
def reset():
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
