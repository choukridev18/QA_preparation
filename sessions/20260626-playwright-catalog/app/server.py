from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS: list[dict] = [
    {"id": 1, "name": "Laptop Pro", "category": "Informatique", "price": 1299.99},
    {"id": 2, "name": "Souris sans fil", "category": "Informatique", "price": 29.99},
    {"id": 3, "name": "Bureau ergonomique", "category": "Mobilier", "price": 349.00},
    {"id": 4, "name": "Chaise de bureau", "category": "Mobilier", "price": 199.00},
    {"id": 5, "name": "Casque audio", "category": "Audio", "price": 89.99},
    {"id": 6, "name": "Enceinte Bluetooth", "category": "Audio", "price": 59.99},
]

CATEGORIES: list[str] = sorted({p["category"] for p in PRODUCTS})


@app.route("/reset")
def reset():
    return "", 204


@app.route("/")
def catalog():
    query = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "").strip()

    results = PRODUCTS
    if query:
        results = [p for p in results if query in p["name"].lower()]
    if category:
        results = [p for p in results if p["category"] == category]

    return render_template(
        "catalog.html",
        products=results,
        categories=CATEGORIES,
        query=query,
        selected_category=category,
        total=len(results),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
