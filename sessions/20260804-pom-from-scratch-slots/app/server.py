from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "qa-slots-secret"

SLOTS = [
    {"id": "slot-1", "label": "Lundi 9h00"},
    {"id": "slot-2", "label": "Lundi 11h00"},
    {"id": "slot-3", "label": "Mardi 9h00"},
    {"id": "slot-4", "label": "Mardi 14h00"},
    {"id": "slot-5", "label": "Mercredi 10h00"},
]

bookings = {}


@app.route("/")
def index():
    booked_slot_id = session.get("booked_slot_id")
    return render_template("slots.html", slots=SLOTS, bookings=bookings, booked_slot_id=booked_slot_id)


@app.route("/book", methods=["POST"])
def book():
    slot_id = request.form.get("slot_id")

    if session.get("booked_slot_id"):
        error = "Vous avez déjà une réservation en cours."
        return render_template("slots.html", slots=SLOTS, bookings=bookings, error=error, booked_slot_id=session.get("booked_slot_id"))

    if not slot_id:
        error = "Veuillez sélectionner un créneau."
        return render_template("slots.html", slots=SLOTS, bookings=bookings, error=error)

    if slot_id in bookings:
        error = "Ce créneau est déjà réservé."
        return render_template("slots.html", slots=SLOTS, bookings=bookings, error=error)

    name = session.get("name", "Utilisateur")
    bookings[slot_id] = name
    session["booked_slot_id"] = slot_id
    return redirect(url_for("confirmation", slot_id=slot_id))


@app.route("/confirmation/<slot_id>")
def confirmation(slot_id):
    slot = next((s for s in SLOTS if s["id"] == slot_id), None)
    if not slot:
        return redirect(url_for("index"))
    return render_template("confirmation.html", slot=slot)


@app.route("/cancel", methods=["POST"])
def cancel():
    slot_id = session.pop("booked_slot_id", None)
    if slot_id and slot_id in bookings:
        del bookings[slot_id]
    return redirect(url_for("index"))


@app.route("/reset", methods=["GET", "POST"])
def reset():
    global bookings
    bookings = {}
    session.clear()
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
