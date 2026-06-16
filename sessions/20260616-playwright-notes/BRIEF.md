# Session Playwright — Éditeur de notes

## Contexte

Une mini app Flask de gestion de notes personnelles est déjà construite. Elle permet de lister, créer, modifier et supprimer des notes. Ton rôle : implémenter les Page Objects et écrire des tests E2E pour couvrir ces parcours.

## Lancer le serveur

```bash
cd sessions/20260616-playwright-notes/app
python3 server.py
# App disponible sur http://localhost:5001
```

## Lancer les tests

```bash
cd sessions/20260616-playwright-notes
.venv/bin/pytest tests/ -v
```

## Ce que tu dois tester

- Affichage de la liste des notes
- Création d'une note valide → apparaît dans la liste
- Création sans titre → message d'erreur
- Suppression d'une note → disparaît de la liste
- Modification d'une note → titre mis à jour dans la liste

## Critères d'acceptance

- [ ] Les 5 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`, `get_by_text`)
- [ ] Pas de `time.sleep()` — utilise `expect()`
- [ ] Le POM encapsule toute l'interaction

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Inspecte `app/templates/` pour comprendre le DOM
- Tu peux modifier `pages/` mais pas `tests/`
