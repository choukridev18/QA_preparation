from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"


@app.route("/")
def index():
    return redirect("/step1")


@app.route("/step1", methods=["GET", "POST"])
def step1():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        if not name:
            error = "Le prénom et nom sont obligatoires."
        elif not email:
            error = "L'adresse email est obligatoire."
        elif "@" not in email:
            error = "L'adresse email n'est pas valide."
        else:
            session["name"] = name
            session["email"] = email
            return redirect("/step2")
    return render_template("step1.html", error=error)


@app.route("/step2", methods=["GET", "POST"])
def step2():
    if "name" not in session:
        return redirect("/step1")
    error = None
    if request.method == "POST":
        date = request.form.get("date", "").strip()
        guests = request.form.get("guests", "").strip()
        if not date:
            error = "La date de réservation est obligatoire."
        else:
            session["date"] = date
            session["guests"] = guests
            return redirect("/confirm")
    return render_template("step2.html", error=error)


@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    if "date" not in session:
        return redirect("/step1")
    if request.method == "POST":
        session["confirmed"] = True
        return redirect("/done")
    return render_template(
        "confirm.html",
        name=session.get("name"),
        email=session.get("email"),
        date=session.get("date"),
        guests=session.get("guests"),
    )


@app.route("/done")
def done():
    if not session.get("confirmed"):
        return redirect("/step1")
    name = session.get("name", "")
    session.clear()
    return render_template("done.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
