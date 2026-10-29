from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "acces-interne-qa"

USERS = {"employe@interne.fr": "qa-demo"}


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if USERS.get(email) == password:
            session["user"] = email
            return redirect("/member")
        error = "Email ou mot de passe incorrect."
    return render_template("login.html", error=error)


@app.route("/member")
def member():
    if "user" not in session:
        return redirect("/login")
    return render_template("member.html", user=session["user"])


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
