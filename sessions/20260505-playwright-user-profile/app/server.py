from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "qa-profile-secret"

# données en mémoire — pas de base de données
PROFILE = {"name": "Marie Dupont", "email": "marie@example.com"}


@app.route("/")
def index():
    return redirect("/profile")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    error = None
    success = session.pop("flash_success", None)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name:
            error = "Le nom est obligatoire."
        elif "@" not in email or "." not in email:
            error = "L'adresse email n'est pas valide."
        else:
            PROFILE["name"] = name
            PROFILE["email"] = email
            session["flash_success"] = "Profil mis à jour avec succès."
            return redirect("/profile")

    return render_template("profile.html", profile=PROFILE, error=error, success=success)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
