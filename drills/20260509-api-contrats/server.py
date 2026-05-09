# NE PAS MODIFIER CE FICHIER
from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = {
    1: {"id": 1, "name": "Stylo", "price": 1.50, "stock": 10},
    2: {"id": 2, "name": "Cahier", "price": 3.00, "stock": 5},
    3: {"id": 3, "name": "Règle",  "price": 2.00, "stock": 0},
}

orders: list[dict] = []
next_order_id: int = 1


@app.route("/products", methods=["GET"])
def list_products():
    return jsonify({"products": list(PRODUCTS.values())}), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if not product:
        return jsonify({"error": "Produit introuvable"}), 404
    return jsonify(product), 200


@app.route("/orders", methods=["POST"])
def create_order():
    global next_order_id
    data = request.get_json()

    if not data or "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "product_id et quantity sont requis"}), 400

    product_id = data["product_id"]
    quantity = data["quantity"]

    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify({"error": "quantity doit être un entier positif"}), 422

    product = PRODUCTS.get(product_id)
    if not product:
        return jsonify({"error": "Produit introuvable"}), 404

    if product["stock"] < quantity:
        return jsonify({"error": "Stock insuffisant"}), 409

    order = {
        "id": next_order_id,
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "total": round(product["price"] * quantity, 2),
    }
    orders.append(order)
    next_order_id += 1
    return jsonify(order), 201


@app.route("/orders", methods=["GET"])
def list_orders():
    return jsonify({"orders": orders}), 200


@app.route("/reset", methods=["POST"])
def reset():
    global orders, next_order_id
    orders.clear()
    next_order_id = 1
    return "", 204
