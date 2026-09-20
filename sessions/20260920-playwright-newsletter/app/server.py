from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

CATEGORIES = [
    ("tech", "Technologie"),
    ("culture", "Culture"),
    ("sport", "Sport"),
]

FREQUENCIES = [
    ("daily", "Quotidienne"),
    ("weekly", "Hebdomadaire"),
    ("monthly", "Mensuelle"),
]

# Preferénces en mémoire (resettable pour les tests)
preferences = {
    "email": "",
    "categories": [],
    "frequency": "",
}


def reset_state():
    preferences["email"] = ""
    preferences["categories"] = []
    preferences["frequency"] = ""
    session.clear()


@app.route("/")
def index():
    return redirect("/preferences")


@app.route("/preferences", methods=["GET", "POST"])
def preferences_page():
    error = None
    success = None

    if request.method == "POST":
        email = (request.form.get("email") or "").strip()
        categories = request.form.getlist("categories")
        frequency = (request.form.get("frequency") or "").strip()

        if not email:
            error = "L'email est obligatoire"
        elif "@" not in email or "." not in email.split("@")[-1]:
            error = "Email invalide"
        elif not categories:
            error = "Choisissez au moins une catégorie"
        elif not frequency:
            error = "Choisissez une fréquence"
        else:
            preferences["email"] = email
            preferences["categories"] = categories
            preferences["frequency"] = frequency
            success = "Préférences enregistrées"

    return render_template(
        "preferences.html",
        error=error,
        success=success,
        categories=CATEGORIES,
        frequencies=FREQUENCIES,
        saved=preferences,
    )


@app.route("/summary")
def summary():
    if not preferences["email"]:
        return redirect("/preferences")
    category_labels = [
        label for key, label in CATEGORIES if key in preferences["categories"]
    ]
    frequency_label = next(
        (label for key, label in FREQUENCIES if key == preferences["frequency"]),
        "",
    )
    return render_template(
        "summary.html",
        email=preferences["email"],
        categories=category_labels,
        frequency=frequency_label,
    )


@app.route("/reset", methods=["POST"])
def reset():
    reset_state()
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
