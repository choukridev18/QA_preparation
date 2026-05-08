# ============================================================
# API Flask — Gestionnaire de tâches
# Déjà implémentée — ne pas modifier.
# Lance : python server.py  (optionnel, pour explorer avec curl/Postman)
# ============================================================

from flask import Flask, jsonify, request

app = Flask(__name__)

tasks: dict[int, dict] = {}
next_id: int = 1


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": list(tasks.values())}), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json(silent=True)
    if not data or not data.get("title"):
        return jsonify({"error": "Le champ 'title' est requis"}), 400
    task = {"id": next_id, "title": data["title"], "done": False}
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Tâche introuvable"}), 404
    return jsonify(task), 200


@app.route("/tasks/<int:task_id>/done", methods=["PATCH"])
def mark_done(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Tâche introuvable"}), 404
    task["done"] = True
    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Tâche introuvable"}), 404
    del tasks[task_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5002)
