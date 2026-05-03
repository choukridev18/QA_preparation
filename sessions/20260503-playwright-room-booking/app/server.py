import secrets
import string
from datetime import date

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "qa-prep-room-booking-secret"


def _generate_reference() -> str:
    suffix = "".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return f"BK-{suffix}"


@app.route("/")
def index():
    return redirect(url_for("booking_step1"))


@app.route("/booking/step1", methods=["GET", "POST"])
def booking_step1():
    error = None
    if request.method == "POST":
        booking_date = request.form.get("booking_date", "").strip()
        room = request.form.get("room", "").strip()
        if not booking_date or not room:
            error = "Veuillez remplir tous les champs obligatoires."
        else:
            session["booking_date"] = booking_date
            session["room"] = room
            return redirect(url_for("booking_step2"))
    today_iso = date.today().isoformat()
    return render_template("booking_step1.html", error=error, today_iso=today_iso)


@app.route("/booking/step2", methods=["GET", "POST"])
def booking_step2():
    if "booking_date" not in session or "room" not in session:
        return redirect(url_for("booking_step1"))

    error = None
    if request.method == "POST":
        time_slot = request.form.get("time_slot", "").strip()
        attendees_raw = request.form.get("attendees", "").strip()
        if not time_slot or not attendees_raw:
            error = "Veuillez remplir tous les champs obligatoires."
        else:
            try:
                attendees = int(attendees_raw)
            except ValueError:
                attendees = 0
            if attendees < 1:
                error = "Le nombre de participants doit être au moins 1."
            else:
                session["time_slot"] = time_slot
                session["attendees"] = attendees
                return redirect(url_for("booking_step3"))

    return render_template("booking_step2.html", error=error)


@app.route("/booking/step3", methods=["GET", "POST"])
def booking_step3():
    required = ("booking_date", "room", "time_slot", "attendees")
    if not all(k in session for k in required):
        if "booking_date" not in session or "room" not in session:
            return redirect(url_for("booking_step1"))
        return redirect(url_for("booking_step2"))

    if request.method == "POST":
        session["booking_ref"] = _generate_reference()
        return redirect(url_for("booking_success"))

    return render_template(
        "booking_step3.html",
        booking_date=session["booking_date"],
        room=session["room"],
        time_slot=session["time_slot"],
        attendees=session["attendees"],
    )


@app.route("/booking/success")
def booking_success():
    ref = session.pop("booking_ref", None)
    if not ref:
        return redirect(url_for("booking_step1"))
    for key in ("booking_date", "room", "time_slot", "attendees"):
        session.pop(key, None)
    return render_template("booking_success.html", reference=ref)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
