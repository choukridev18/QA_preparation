from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)

LIVRAISONS = [
    {
        "id": 1,
        "client": "Alice Martin",
        "adresse": "12 rue de la Paix, Paris",
        "statut": "en cours",
    },
    {
        "id": 2,
        "client": "Bob Dupont",
        "adresse": "7 avenue des Fleurs, Lyon",
        "statut": "livré",
    },
    {
        "id": 3,
        "client": "Clara Moreau",
        "adresse": "3 boulevard Voltaire, Marseille",
        "statut": "en cours",
    },
    {
        "id": 4,
        "client": "David Leroy",
        "adresse": "22 rue Nationale, Lille",
        "statut": "retourné",
    },
    {
        "id": 5,
        "client": "Emma Bernard",
        "adresse": "9 place du Marché, Bordeaux",
        "statut": "en cours",
    },
]

_data = [dict(l) for l in LIVRAISONS]


def get_data():
    return _data


@app.route("/")
def index():
    filtre = request.args.get("statut", "tous")
    if filtre == "tous":
        livraisons = get_data()
    else:
        livraisons = [l for l in get_data() if l["statut"] == filtre]

    counts = {
        "tous": len(get_data()),
        "en cours": sum(1 for l in get_data() if l["statut"] == "en cours"),
        "livré": sum(1 for l in get_data() if l["statut"] == "livré"),
        "retourné": sum(1 for l in get_data() if l["statut"] == "retourné"),
    }
    return render_template(
        "dashboard.html", livraisons=livraisons, filtre=filtre, counts=counts
    )


@app.route("/update/<int:livraison_id>", methods=["POST"])
def update_statut(livraison_id):
    nouveau_statut = request.form.get("statut")
    statuts_valides = ["en cours", "livré", "retourné"]
    if nouveau_statut not in statuts_valides:
        return "Statut invalide", 400
    for l in get_data():
        if l["id"] == livraison_id:
            l["statut"] = nouveau_statut
            break
    return redirect(url_for("index"))


@app.route("/reset", methods=["POST"])
def reset():
    global _data
    _data = [dict(l) for l in LIVRAISONS]
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
