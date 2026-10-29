from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "qa-panier-secret"

PRODUCTS = [
    {"id": "clavier", "name": "Clavier compact", "price": 49.90},
    {"id": "souris", "name": "Souris sans fil", "price": 29.50},
    {"id": "tapis", "name": "Tapis de bureau", "price": 15.00},
]


def _product_by_id(product_id: str):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


def _cart_lines():
    """Liste ordonnée des lignes panier : {id, name, price, quantity}."""
    raw = session.get("cart", {})
    lines = []
    for product_id, qty in raw.items():
        product = _product_by_id(product_id)
        if product and qty > 0:
            lines.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": int(qty),
                }
            )
    return lines


def _cart_count():
    return sum(item["quantity"] for item in _cart_lines())


def _cart_total():
    total = sum(line["price"] * line["quantity"] for line in _cart_lines())
    return round(total, 2)


@app.route("/", methods=["GET"])
def catalog():
    return render_template(
        "catalog.html",
        products=PRODUCTS,
        cart_count=_cart_count(),
    )


@app.route("/cart/add", methods=["POST"])
def cart_add():
    product_id = request.form.get("product_id", "").strip()
    if _product_by_id(product_id):
        cart = session.get("cart", {})
        cart[product_id] = cart.get(product_id, 0) + 1
        session["cart"] = cart
    return redirect("/")


@app.route("/cart", methods=["GET"])
def cart_page():
    return render_template(
        "cart.html",
        lines=_cart_lines(),
        total=_cart_total(),
    )


@app.route("/cart/clear", methods=["POST"])
def cart_clear():
    session.clear()
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
