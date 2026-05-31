from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

USERS = {
    "admin@example.com": "password123",
    "user@example.com": "secret456",
}


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        if not email or not password:
            error = "Veuillez remplir tous les champs."
        elif USERS.get(email) == password:
            session["user"] = email
            return redirect("/dashboard")
        else:
            error = "Identifiants incorrects."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", email=session["user"])


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
