from flask import Flask, render_template, request

app = Flask(__name__)

COLLEAGUES = [
    "Léa Martin",
    "Karim Benali",
    "Emma Rossi",
    "Noah Bernard",
    "Inès Moreau",
]


@app.route("/", methods=["GET"])
def directory():
    query = request.args.get("q", "").strip()
    if query:
        results = [name for name in COLLEAGUES if query.lower() in name.lower()]
    else:
        results = list(COLLEAGUES)
    return render_template("directory.html", query=query, results=results)


@app.route("/reset", methods=["POST"])
def reset():
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
