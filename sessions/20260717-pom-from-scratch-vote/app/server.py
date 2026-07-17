from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "qa-vote-secret"

OPTIONS = ["Python", "JavaScript", "Java", "Go"]

votes = {option: 0 for option in OPTIONS}


@app.route("/")
def index():
    error = request.args.get("error")
    return render_template("vote.html", options=OPTIONS, error=error)


@app.route("/vote", methods=["POST"])
def vote():
    if session.get("voted"):
        return render_template(
            "vote.html",
            options=OPTIONS,
            error="Vous avez déjà voté.",
        )

    choice = request.form.get("choice")
    if not choice:
        return render_template(
            "vote.html",
            options=OPTIONS,
            error="Veuillez sélectionner une option avant de voter.",
        )

    if choice not in votes:
        return render_template(
            "vote.html",
            options=OPTIONS,
            error="Option invalide.",
        )

    votes[choice] += 1
    session["voted"] = True
    return redirect(url_for("results"))


@app.route("/results")
def results():
    total = sum(votes.values())
    results_data = []
    for option in OPTIONS:
        count = votes[option]
        pct = round(count / total * 100) if total > 0 else 0
        results_data.append({"option": option, "count": count, "pct": pct})
    return render_template("results.html", results=results_data, total=total)


@app.route("/vote-again")
def vote_again():
    session.pop("voted", None)
    return redirect(url_for("index"))


@app.route("/reset", methods=["GET", "POST"])
def reset():
    global votes
    votes = {option: 0 for option in OPTIONS}
    session.clear()
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
