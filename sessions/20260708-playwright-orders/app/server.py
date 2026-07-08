import copy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

INITIAL_ORDERS = [
    {"id": 1, "client": "Alice Martin",  "amount": 45.90,  "status": "en attente"},
    {"id": 2, "client": "Bob Dupont",    "amount": 120.00, "status": "expédiée"},
    {"id": 3, "client": "Carol Blanc",   "amount": 89.50,  "status": "livrée"},
    {"id": 4, "client": "David Noir",    "amount": 33.00,  "status": "en attente"},
    {"id": 5, "client": "Emma Vert",     "amount": 210.75, "status": "livrée"},
]

orders = copy.deepcopy(INITIAL_ORDERS)


@app.route("/")
def index():
    status_filter = request.args.get("status", "")
    if status_filter:
        visible = [o for o in orders if o["status"] == status_filter]
    else:
        visible = orders

    counts = {
        "en attente": sum(1 for o in orders if o["status"] == "en attente"),
        "expédiée":   sum(1 for o in orders if o["status"] == "expédiée"),
        "livrée":     sum(1 for o in orders if o["status"] == "livrée"),
    }

    return render_template(
        "orders.html",
        orders=visible,
        counts=counts,
        current_filter=status_filter,
    )


@app.route("/orders/<int:order_id>/status", methods=["POST"])
def update_status(order_id):
    new_status = request.form.get("status")
    for o in orders:
        if o["id"] == order_id:
            o["status"] = new_status
            break
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    global orders
    orders = copy.deepcopy(INITIAL_ORDERS)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)
