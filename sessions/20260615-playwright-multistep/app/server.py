from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

PLANS = ["Gratuit", "Pro", "Entreprise"]


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return "", 204


@app.route("/")
def index():
    return redirect(url_for("step1"))


@app.route("/step1", methods=["GET"])
def step1():
    return render_template("step1.html", errors={}, form=session.get("step1", {}))


@app.route("/step1", methods=["POST"])
def step1_post():
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    email = request.form.get("email", "").strip()

    errors = {}
    if not first_name:
        errors["first_name"] = "Le prénom est requis."
    if not last_name:
        errors["last_name"] = "Le nom est requis."
    if not email or "@" not in email:
        errors["email"] = "Un email valide est requis."

    if errors:
        form = {"first_name": first_name, "last_name": last_name, "email": email}
        return render_template("step1.html", errors=errors, form=form), 422

    session["step1"] = {"first_name": first_name, "last_name": last_name, "email": email}
    return redirect(url_for("step2"))


@app.route("/step2", methods=["GET"])
def step2():
    if "step1" not in session:
        return redirect(url_for("step1"))
    return render_template("step2.html", plans=PLANS, errors={}, selected=session.get("step2", {}).get("plan", ""))


@app.route("/step2", methods=["POST"])
def step2_post():
    plan = request.form.get("plan", "").strip()

    errors = {}
    if not plan or plan not in PLANS:
        errors["plan"] = "Choisissez un plan valide."

    if errors:
        return render_template("step2.html", plans=PLANS, errors=errors, selected=plan), 422

    session["step2"] = {"plan": plan}
    return redirect(url_for("confirm"))


@app.route("/confirm", methods=["GET"])
def confirm():
    if "step1" not in session or "step2" not in session:
        return redirect(url_for("step1"))
    data = {**session["step1"], **session["step2"]}
    return render_template("confirm.html", data=data)


@app.route("/confirm", methods=["POST"])
def confirm_post():
    session["submitted"] = True
    session.clear()
    return redirect(url_for("success"))


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
