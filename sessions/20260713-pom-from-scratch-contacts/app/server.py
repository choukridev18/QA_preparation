import copy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "qa-prep-secret"

INITIAL_CONTACTS = [
    {"id": 1, "name": "Alice Martin",  "email": "alice@example.com",  "phone": "0601020304"},
    {"id": 2, "name": "Bob Dupont",    "email": "bob@example.com",    "phone": "0605060708"},
    {"id": 3, "name": "Carol Blanc",   "email": "carol@example.com",  "phone": "0609101112"},
]

contacts = copy.deepcopy(INITIAL_CONTACTS)
next_id = 4


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    if query:
        visible = [c for c in contacts if query.lower() in c["name"].lower()]
    else:
        visible = contacts
    return render_template("contacts.html", contacts=visible, query=query)


@app.route("/contacts/add", methods=["POST"])
def add_contact():
    global next_id
    name  = request.form.get("name",  "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()

    error = None
    if not name:
        error = "Le nom est obligatoire."
    elif not email or "@" not in email:
        error = "L'adresse email est invalide."
    elif any(c["email"] == email for c in contacts):
        error = "Cet email est déjà utilisé."

    if error:
        return render_template("contacts.html", contacts=contacts, query="", error=error)

    contacts.append({"id": next_id, "name": name, "email": email, "phone": phone})
    next_id += 1
    return redirect("/")


@app.route("/contacts/<int:contact_id>/delete", methods=["POST"])
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c["id"] != contact_id]
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    global contacts, next_id
    contacts = copy.deepcopy(INITIAL_CONTACTS)
    next_id = 4
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5001)
