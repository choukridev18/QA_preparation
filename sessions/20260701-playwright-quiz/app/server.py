from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

QUESTIONS = [
    {
        "text": "Quelle est la capitale de la France ?",
        "choices": ["Londres", "Berlin", "Paris", "Madrid"],
        "correct": "Paris",
    },
    {
        "text": "Combien font 7 × 8 ?",
        "choices": ["54", "56", "48", "64"],
        "correct": "56",
    },
    {
        "text": "Quel est le plus grand océan du monde ?",
        "choices": ["Atlantique", "Indien", "Arctique", "Pacifique"],
        "correct": "Pacifique",
    },
]


@app.route("/")
def index():
    session.clear()
    return redirect("/quiz/1")


@app.route("/quiz/<int:n>", methods=["GET", "POST"])
def question(n):
    if n < 1 or n > len(QUESTIONS):
        return redirect("/")

    if request.method == "POST":
        answer = request.form.get("answer")
        answers = session.get("answers", [])
        answers.append(answer)
        session["answers"] = answers

        if n < len(QUESTIONS):
            return redirect(f"/quiz/{n + 1}")
        return redirect("/quiz/result")

    q = QUESTIONS[n - 1]
    return render_template("question.html", question=q, number=n, total=len(QUESTIONS))


@app.route("/quiz/result")
def result():
    answers = session.get("answers", [])
    answers = answers[:len(QUESTIONS)]
    score = sum(
        1 for i, ans in enumerate(answers) if ans == QUESTIONS[i]["correct"]
    )
    return render_template("result.html", score=score, total=len(QUESTIONS))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
