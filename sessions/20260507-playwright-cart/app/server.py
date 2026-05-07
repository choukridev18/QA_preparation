from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

PRODUCTS = [
    {"id": 1, "name": "Clavier mécanique", "price": 89.99},
    {"id": 2, "name": "Souris ergonomique", "price": 45.50},
    {"id": 3, "name": "Écran 27 pouces", "price": 299.00},
    {"id": 4, "name": "Casque audio", "price": 75.00},
]


def get_product_by_id(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


@app.route("/")
def catalog():
    cart_count = sum(session.get("cart", {}).values())
    return render_template("catalog.html", products=PRODUCTS, cart_count=cart_count)


@app.route("/cart")
def cart():
    cart_data = session.get("cart", {})
    items = []
    total = 0.0
    for product_id_str, quantity in cart_data.items():
        product = get_product_by_id(int(product_id_str))
        if product:
            subtotal = round(product["price"] * quantity, 2)
            total += subtotal
            items.append({**product, "quantity": quantity, "subtotal": subtotal})
    total = round(total, 2)
    return render_template("cart.html", items=items, total=total)


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
    quantity = int(request.form.get("quantity", 1))
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    session["cart"] = cart
    return redirect("/")


@app.route("/cart/update", methods=["POST"])
def update_cart():
    product_id = request.form.get("product_id")
    quantity = int(request.form.get("quantity", 1))
    cart = session.get("cart", {})
    if str(product_id) in cart:
        cart[str(product_id)] = max(1, quantity)
        session["cart"] = cart
    return redirect("/cart")


@app.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    product_id = request.form.get("product_id")
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    return redirect("/cart")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
