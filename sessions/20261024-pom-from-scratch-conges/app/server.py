from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "qa-prep-secret"


@app.route("/", methods=["GET", "POST"])
def leave_form():
    error = ""

    if request.method == "POST":
        start_date = request.form.get("start_date", "").strip()
        end_date = request.form.get("end_date", "").strip()
        reason = request.form.get("reason", "").strip()

        if not start_date:
            error = "La date de début est obligatoire."
        elif not end_date:
            error = "La date de fin est obligatoire."
        elif not reason:
            error = "Le motif est obligatoire."
        elif end_date < start_date:
            error = "La date de fin doit être après la date de début."
        else:
            session["leave"] = {
                "start_date": start_date,
                "end_date": end_date,
                "reason": reason,
            }
            return redirect(url_for("confirmation"))

    return render_template("leave.html", error=error)


@app.route("/confirmation")
def confirmation():
    leave = session.get("leave")
    if not leave:
        return redirect(url_for("leave_form"))
    return render_template("confirmation.html", leave=leave)


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
