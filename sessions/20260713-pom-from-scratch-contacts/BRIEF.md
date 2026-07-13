# Session Playwright — Gestionnaire de contacts (from scratch)

## Contexte

Une app de gestion de contacts est déjà construite. Elle affiche 3 contacts initiaux (nom, email, téléphone). Tu peux ajouter un contact, rechercher par nom et supprimer un contact. **Aucun Page Object ni aucun test n'est fourni** — tu crées tout toi-même.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://127.0.0.1:5001
```

## Ce que tu dois faire

1. Lire `app/templates/contacts.html` pour comprendre le DOM
2. Créer `pages/contacts_page.py` avec une classe `ContactsPage`
3. Créer `tests/test_contacts.py` avec tes tests

## Critères d'acceptance

- [ ] Au moins 5 tests couvrant des parcours différents
- [ ] Ajout d'un contact valide → il apparaît dans la liste
- [ ] Email déjà utilisé → message d'erreur affiché
- [ ] Champ nom vide → message d'erreur affiché
- [ ] Recherche par nom → filtre la liste
- [ ] Suppression d'un contact → il disparaît de la liste
- [ ] Locators sémantiques (`get_by_label`, `get_by_role`) — pas de CSS fragile
- [ ] Pas de `time.sleep()`
- [ ] Tout passe avec `pytest tests/ -v`

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire — une classe par écran
- `pages/` et `tests/` sont vides — tout est à toi
- Inspecte `app/templates/contacts.html` avant d'écrire le moindre locator
