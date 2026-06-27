from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

REGISTERED_EMAILS = set()


@app.route("/")
def index():
    return redirect("/signup/step1")


@app.route("/signup/step1", methods=["GET", "POST"])
def step1():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name:
            error = "Le nom est obligatoire."
        elif not email or "@" not in email:
            error = "L'adresse email est invalide."
        elif email in REGISTERED_EMAILS:
            error = "Cet email est déjà utilisé."
        elif len(password) < 6:
            error = "Le mot de passe doit contenir au moins 6 caractères."
        else:
            session["signup"] = {"name": name, "email": email, "password": password}
            return redirect("/signup/step2")

    return render_template("step1.html", error=error)


@app.route("/signup/step2", methods=["GET", "POST"])
def step2():
    if "signup" not in session:
        return redirect("/signup/step1")

    if request.method == "POST":
        newsletter = request.form.get("newsletter") == "on"
        language = request.form.get("language", "fr")
        session["signup"]["newsletter"] = newsletter
        session["signup"]["language"] = language
        REGISTERED_EMAILS.add(session["signup"]["email"])
        name = session["signup"]["name"]
        session.pop("signup", None)
        return redirect(f"/signup/confirm?name={name}")

    return render_template("step2.html")


@app.route("/signup/confirm")
def confirm():
    name = request.args.get("name", "")
    return render_template("confirm.html", name=name)


@app.route("/reset", methods=["POST"])
def reset():
    REGISTERED_EMAILS.clear()
    session.clear()
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)
