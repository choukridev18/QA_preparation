from flask import Flask, render_template, request, redirect

app = Flask(__name__)

TICKETS: list[dict] = []


@app.route("/", methods=["GET", "POST"])
def index():
    success = None
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        priority = request.form.get("priority", "")
        description = request.form.get("description", "").strip()
        if subject and priority and description:
            TICKETS.append(
                {
                    "subject": subject,
                    "priority": priority,
                    "description": description,
                }
            )
            success = "Ticket créé avec succès."
            return render_template(
                "support.html", tickets=TICKETS, success=success
            )
    return render_template("support.html", tickets=TICKETS, success=success)


@app.route("/reset", methods=["POST"])
def reset():
    TICKETS.clear()
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)