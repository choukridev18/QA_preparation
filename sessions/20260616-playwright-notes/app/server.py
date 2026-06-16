from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

NOTES: list[dict] = [
    {"id": 1, "title": "Réunion équipe", "content": "Préparer l'ordre du jour pour lundi."},
    {"id": 2, "title": "Idées projet", "content": "Utiliser Playwright pour les tests E2E."},
]
_next_id = 3


def _find_note(note_id: int) -> dict | None:
    return next((n for n in NOTES if n["id"] == note_id), None)


@app.route("/reset")
def reset():
    global NOTES, _next_id
    NOTES = [
        {"id": 1, "title": "Réunion équipe", "content": "Préparer l'ordre du jour pour lundi."},
        {"id": 2, "title": "Idées projet", "content": "Utiliser Playwright pour les tests E2E."},
    ]
    _next_id = 3
    return "", 204


@app.route("/")
def index():
    return render_template("notes.html", notes=NOTES)


@app.route("/new", methods=["GET", "POST"])
def new_note():
    global _next_id
    error_title = None
    error_content = None
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if not title:
            error_title = "Le titre est obligatoire."
        if not content:
            error_content = "Le contenu est obligatoire."
        if not error_title and not error_content:
            NOTES.append({"id": _next_id, "title": title, "content": content})
            _next_id += 1
            return redirect(url_for("index"))
    return render_template("new_note.html", error_title=error_title, error_content=error_content)


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id: int):
    note = _find_note(note_id)
    if note is None:
        return redirect(url_for("index"))
    error_title = None
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if not title:
            error_title = "Le titre est obligatoire."
        else:
            note["title"] = title
            note["content"] = content
            return redirect(url_for("index"))
    return render_template("edit_note.html", note=note, error_title=error_title)


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id: int):
    global NOTES
    NOTES = [n for n in NOTES if n["id"] != note_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
