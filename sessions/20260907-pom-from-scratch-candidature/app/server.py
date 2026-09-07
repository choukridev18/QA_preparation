from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "candidature-secret"


@app.route("/")
def index():
    return redirect(url_for("step1"))


@app.route("/step1", methods=["GET", "POST"])
def step1():
    error = None
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        email = request.form.get("email", "").strip()
        telephone = request.form.get("telephone", "").strip()

        if not nom:
            error = "Le nom est obligatoire."
        elif not email or "@" not in email:
            error = "L'adresse email est invalide."
        elif not telephone:
            error = "Le téléphone est obligatoire."
        else:
            session["step1"] = {"nom": nom, "email": email, "telephone": telephone}
            return redirect(url_for("step2"))

    return render_template("step1.html", error=error)


@app.route("/step2", methods=["GET", "POST"])
def step2():
    if "step1" not in session:
        return redirect(url_for("step1"))

    error = None
    if request.method == "POST":
        poste = request.form.get("poste", "").strip()
        experience = request.form.get("experience", "").strip()
        motivation = request.form.get("motivation", "").strip()

        if not poste:
            error = "Le poste visé est obligatoire."
        elif not experience:
            error = "L'expérience est obligatoire."
        elif len(motivation) < 20:
            error = "La motivation doit faire au moins 20 caractères."
        else:
            session["step2"] = {"poste": poste, "experience": experience, "motivation": motivation}
            return redirect(url_for("confirmation"))

    return render_template("step2.html", error=error)


@app.route("/confirmation")
def confirmation():
    if "step1" not in session or "step2" not in session:
        return redirect(url_for("step1"))

    data = {**session["step1"], **session["step2"]}
    return render_template("confirmation.html", data=data)


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
