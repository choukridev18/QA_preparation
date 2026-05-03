import secrets
import string

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "qa-pom-from-scratch-visitor-secret"


def _generate_badge_id() -> str:
    suffix = "".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return f"BADGE-{suffix}"


@app.route("/")
def index():
    return redirect(url_for("visitor_step1"))


@app.route("/visitor/step1", methods=["GET", "POST"])
def visitor_step1():
    error = None
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        company = request.form.get("company", "").strip()
        if not full_name or not email or not company:
            error = "Tous les champs sont obligatoires."
        else:
            session["full_name"] = full_name
            session["email"] = email
            session["company"] = company
            return redirect(url_for("visitor_step2"))
    return render_template("visitor_step1.html", error=error)


@app.route("/visitor/step2", methods=["GET", "POST"])
def visitor_step2():
    if "full_name" not in session or "email" not in session or "company" not in session:
        return redirect(url_for("visitor_step1"))

    error = None
    if request.method == "POST":
        visit_date = request.form.get("visit_date", "").strip()
        purpose = request.form.get("purpose", "").strip()
        if not visit_date or not purpose:
            error = "Tous les champs sont obligatoires."
        else:
            session["visit_date"] = visit_date
            session["purpose"] = purpose
            return redirect(url_for("visitor_step3"))

    return render_template("visitor_step2.html", error=error)


@app.route("/visitor/step3", methods=["GET", "POST"])
def visitor_step3():
    required = ("full_name", "email", "company", "visit_date", "purpose")
    if not all(k in session for k in required):
        if "full_name" not in session:
            return redirect(url_for("visitor_step1"))
        return redirect(url_for("visitor_step2"))

    if request.method == "POST":
        session["badge_id"] = _generate_badge_id()
        return redirect(url_for("visitor_success"))

    return render_template(
        "visitor_step3.html",
        full_name=session["full_name"],
        email=session["email"],
        company=session["company"],
        visit_date=session["visit_date"],
        purpose=session["purpose"],
    )


@app.route("/visitor/success")
def visitor_success():
    badge = session.pop("badge_id", None)
    if not badge:
        return redirect(url_for("visitor_step1"))
    for key in ("full_name", "email", "company", "visit_date", "purpose"):
        session.pop(key, None)
    return render_template("visitor_success.html", badge_id=badge)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
