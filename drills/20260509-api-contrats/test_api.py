# ============================================================
# DRILL — pytest.mark.parametrize · pytest.raises · contrats API
# ============================================================
# Contexte :
#   Une API e-commerce gère des produits et des commandes.
#   Tu dois vérifier que l'API respecte son contrat : bons champs,
#   bons types, bons codes HTTP, bonnes erreurs.
#
# Objectif :
#   Implémenter les TODOs ci-dessous pour que tous les tests passent.
#   Lance : pytest test_api.py -v
# ============================================================

import pytest
from werkzeug.wrappers import response



# ------------------------------------------------------------
# TODO 1 — Vérifier la structure de la liste des produits
# ------------------------------------------------------------
# GET /products doit retourner 200 et un body avec une clé "products"
# qui contient une liste de dicts ayant chacun les clés "id", "name", "price", "stock"
# ------------------------------------------------------------
def test_products_list_has_correct_structure(client):
    response= client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert "products" in data
    assert "id" in data["products"][0]
    assert "name" in data["products"][0]
    assert "price" in data["products"][0]
    assert "stock" in data["products"][0]


# ------------------------------------------------------------
# TODO 2 — Récupérer un produit par son ID
# ------------------------------------------------------------
# GET /products/1 doit retourner 200 et un body avec les clés
# "id", "name", "price", "stock" — et "id" doit valoir 1
# ------------------------------------------------------------
def test_get_product_returns_correct_fields(client):
    response=  client.get("/products/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "name" in data
    assert "price" in data
    assert "stock" in data


# ------------------------------------------------------------
# TODO 3 — Produit inexistant retourne 404
# ------------------------------------------------------------
# GET /products/999 doit retourner 404 et un body avec "error"
# ------------------------------------------------------------
def test_get_unknown_product_returns_404(client):
    response = client.get("/products/999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] 


# ------------------------------------------------------------
# TODO 4 — Créer une commande valide
# ------------------------------------------------------------
# POST /orders avec {"product_id": 1, "quantity": 2}
# doit retourner 201 et un body avec "id", "product_id",
# "product_name", "quantity", "total"
# Le total doit valoir 3.0 (1.50 × 2)
# ------------------------------------------------------------
def test_create_order_returns_correct_body(client):
    response = client.post("/orders",json={"product_id": 1, "quantity":2})
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert "product_id" in data
    assert "product_name" in data
    assert "quantity" in data
    assert data["total"] == 3.0


# ------------------------------------------------------------
# TODO 5 — Commande avec champs manquants retourne 400
# ------------------------------------------------------------
# Utilise @pytest.mark.parametrize pour tester 3 cas :
#   - body vide {}
#   - body sans quantity : {"product_id": 1}
#   - body sans product_id : {"quantity": 2}
# Chaque cas doit retourner 400
# ------------------------------------------------------------
@pytest.mark.parametrize("payload", [{},{"product_id":1},{"quantity":2}
    # TODO : remplis les 3 cas

])
def test_create_order_missing_fields_returns_400(client, payload):
    response = client.post("/orders",json= payload)
    assert response.status_code == 400
    


# ------------------------------------------------------------
# TODO 6 — Quantity invalide retourne 422
# ------------------------------------------------------------
# Utilise @pytest.mark.parametrize pour tester 3 cas :
#   - quantity = 0
#   - quantity = -1
#   - quantity = "deux" (string)
# Chaque cas doit retourner 422
# ------------------------------------------------------------
@pytest.mark.parametrize("quantity", [
    0,-1,"deux"
    
])
def test_create_order_invalid_quantity_returns_422(client, quantity):
    response = client.post("/orders",json={"product_id":1, "quantity":quantity} )
    assert response.status_code == 422



# ------------------------------------------------------------
# TODO 7 — Produit en rupture de stock retourne 409
# ------------------------------------------------------------
# Le produit id=3 ("Règle") a un stock de 0
# POST /orders avec {"product_id": 3, "quantity": 1}
# doit retourner 409 et un body avec "error"
# ------------------------------------------------------------
def test_create_order_out_of_stock_returns_409(client):
    response = client.post("/orders",json= {"product_id":3,"quantity":8})
    assert response.status_code == 409
    data = response.get_json()
    assert data["error"]


# ------------------------------------------------------------
# TODO 8 — La liste des commandes se met à jour
# ------------------------------------------------------------
# Créer 2 commandes, puis GET /orders
# doit retourner 200 et une liste de 2 commandes
# ------------------------------------------------------------
def test_orders_list_grows_after_two_orders(client):
    command1= client.post("/orders",json= {"product_id":1,"quantity":8})
    command2= client.post("/orders",json= {"product_id":2,"quantity":4})
    response = client.get("/orders")
    data = response.get_json()
    assert len(data["orders"]) == 2
    
    
