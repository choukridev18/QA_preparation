from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

DEFAULT_PROFILE = {
    "name": "Alice Martin",
    "email": "alice@example.com",
    "bio": "Développeuse passionnée.",
}

PROFILE = dict(DEFAULT_PROFILE)


@app.route("/reset", methods=["POST"])
def reset():
    global PROFILE
    PROFILE = dict(DEFAULT_PROFILE)
    return "", 204


@app.route("/")
def index():
    return redirect(url_for("profile"))


@app.route("/profile", methods=["GET"])
def profile():
    return render_template("profile.html", profile=PROFILE, success=None, errors={})


@app.route("/profile/edit", methods=["GET"])
def profile_edit():
    return render_template("edit.html", profile=PROFILE, errors={})


@app.route("/profile/edit", methods=["POST"])
def profile_edit_post():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    bio = request.form.get("bio", "").strip()

    errors = {}

    if not name:
        errors["name"] = "Le nom est requis."

    if not email:
        errors["email"] = "L'email est requis."
    elif "@" not in email or "." not in email.split("@")[-1]:
        errors["email"] = "L'email n'est pas valide."

    if errors:
        form_data = {"name": name, "email": email, "bio": bio}
        return render_template("edit.html", profile=form_data, errors=errors), 422

    PROFILE["name"] = name
    PROFILE["email"] = email
    PROFILE["bio"] = bio

    session["success"] = True
    return redirect(url_for("profile"))


@app.route("/profile", methods=["POST"])
def profile_post():
    success = session.pop("success", False)
    return render_template("profile.html", profile=PROFILE, success=success, errors={})


@app.context_processor
def inject_success():
    success = session.pop("success", False)
    return {"flash_success": success}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
