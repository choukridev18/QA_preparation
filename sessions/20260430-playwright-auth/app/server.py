from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

USERS = {"alice@example.com": "password123"}


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        if USERS.get(email) == password:
            session["user"] = email
            return redirect("/dashboard")
        error = "Identifiants incorrects. Veuillez réessayer."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/login")


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)
