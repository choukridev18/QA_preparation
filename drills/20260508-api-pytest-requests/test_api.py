# ============================================================
# DRILL — Tests API REST avec Flask test client
# ============================================================
# Contexte :
#   Tu testes une API de gestion de tâches (server.py).
#   Pas besoin de lancer le serveur — le client de test Flask
#   simule les requêtes HTTP directement.
#
# Référence du client de test Flask :
#   client.get("/tasks")                          → GET /tasks
#   client.post("/tasks", json={"title": "..."})  → POST /tasks
#   client.patch("/tasks/1/done")                 → PATCH /tasks/1/done
#   client.delete("/tasks/1")                     → DELETE /tasks/1
#   response.status_code                          → code HTTP (200, 201, 404…)
#   response.get_json()                           → body parsé en dict
#
# Lance : pytest drills/20260508-api-pytest-requests/test_api.py -v
# ============================================================


# ------------------------------------------------------------------
# TODO 1 — GET /tasks sur une API vide
# ------------------------------------------------------------------
# Attendu : status 200, body = {"tasks": []}
# ------------------------------------------------------------------
import json
from werkzeug.wrappers import response


def test_get_tasks_returns_empty_list(client):
    """GET /tasks renvoie une liste vide au démarrage"""

    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert data["tasks"] == []
    


# ------------------------------------------------------------------
# TODO 2 — POST /tasks crée une nouvelle tâche
# ------------------------------------------------------------------
# Entrée  : {"title": "Faire les courses"}
# Attendu : status 201, body contient "id", "title", "done": False
# ------------------------------------------------------------------
def test_create_task_returns_201_with_body(client):
    """POST /tasks retourne 201 et le body de la tâche créée"""
    create = client.post("/tasks",json= {"title":"Faire les courses"})
    assert create.status_code == 201
    data = create.get_json()
    assert data["title"] == "Faire les courses"
    assert data["done"] == False
    assert "id" in data
    
    


# ------------------------------------------------------------------
# TODO 3 — GET /tasks/<id> retourne la bonne tâche
# ------------------------------------------------------------------
# Étapes : créer une tâche, puis la récupérer par son id
# Attendu : status 200, title correct
# ------------------------------------------------------------------
def test_get_task_by_id_returns_correct_task(client):
    """GET /tasks/<id> retourne la tâche correspondante"""
    create = client.post("/tasks",json={"title":"Ma tache"})
    task_id = create.get_json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Ma tache"



# ------------------------------------------------------------------
# TODO 4 — GET /tasks/<id> sur un id inexistant
# ------------------------------------------------------------------
# Attendu : status 404
# ------------------------------------------------------------------
def test_get_unknown_task_returns_404(client):
    """GET /tasks/9999 retourne 404"""
    response = client.get("/tasks/9999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"]== "Tâche introuvable"



# ------------------------------------------------------------------
# TODO 5 — POST /tasks sans title
# ------------------------------------------------------------------
# Attendu : status 400
# ------------------------------------------------------------------
def test_create_task_without_title_returns_400(client):
    """POST /tasks sans champ title retourne 400"""
    create = client.post("/tasks",json={"title":""})
    assert create.status_code == 400
    data = create.get_json()
    assert data["error"] =="Le champ 'title' est requis"
    
    


# ------------------------------------------------------------------
# TODO 6 — PATCH /tasks/<id>/done marque la tâche comme terminée
# ------------------------------------------------------------------
# Étapes : créer une tâche, la marquer done
# Attendu : status 200, done = True dans le body
# ------------------------------------------------------------------
def test_mark_task_as_done(client):
    """PATCH /tasks/<id>/done passe done à True"""
    create = client.post("/tasks",json={"title":"Ma tache"})
    task_id= create.get_json()["id"]
    
    response = client.patch(f"/tasks/{task_id}/done")
    assert response.status_code == 200
    data = response.get_json()
    assert data["done"] == True
    


# ------------------------------------------------------------------
# TODO 7 — DELETE /tasks/<id> supprime la tâche
# ------------------------------------------------------------------
# Étapes  : créer, supprimer, puis GET → vérifier 404
# Attendu : DELETE retourne 204, GET retourne 404 ensuite
# ------------------------------------------------------------------
def test_delete_task_returns_204_and_removes_it(client):
    """DELETE /tasks/<id> retourne 204 et la tâche n'est plus accessible"""
    create = client.post("/tasks",json={"title":"à supprimer"})
    assert create.status_code == 201
    task_id = create.get_json()["id"]

    delete= client.delete(f"/tasks/{task_id}")
    assert delete.status_code == 204

    get = client.get(f"/tasks/{task_id}")
    assert get.status_code == 404




# ------------------------------------------------------------------
# TODO 8 — DELETE /tasks/<id> sur un id inexistant
# ------------------------------------------------------------------
# Attendu : status 404
# ------------------------------------------------------------------
def test_delete_unknown_task_returns_404(client):
    """DELETE /tasks/9999 retourne 404"""
    delete = client.delete("/tasks/9999")
    assert delete.status_code == 404
