from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS: list[dict] = []
_next_id = 1


def _pending_count() -> int:
    return sum(1 for t in TASKS if not t["done"])


@app.route("/", methods=["GET", "POST"])
def index():
    global _next_id
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            TASKS.append({"id": _next_id, "title": title, "done": False})
            _next_id += 1
        return redirect(url_for("index"))
    return render_template(
        "tasks.html",
        tasks=TASKS,
        pending=_pending_count(),
    )


@app.route("/complete", methods=["POST"])
def complete():
    todo_id = int(request.form.get("todo_id", 0))
    for task in TASKS:
        if task["id"] == todo_id:
            task["done"] = True
            break
    return redirect(url_for("index"))


@app.route("/reset", methods=["POST"])
def reset():
    global _next_id
    TASKS.clear()
    _next_id = 1
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)