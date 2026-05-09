from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

todos: list[dict] = []
next_id: int = 1


@app.route("/")
def index():
    filtre = request.args.get("filter", "all")
    if filtre == "active":
        visible = [t for t in todos if not t["done"]]
    elif filtre == "done":
        visible = [t for t in todos if t["done"]]
    else:
        visible = todos
    return render_template("index.html", todos=visible, filtre=filtre, total=len(todos))


@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        todos.append({"id": next_id, "title": title, "done": False})
        next_id += 1
    return redirect("/")


@app.route("/done/<int:todo_id>", methods=["POST"])
def mark_done(todo_id):
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            break
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    global todos, next_id
    todos.clear()
    next_id = 1
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)
