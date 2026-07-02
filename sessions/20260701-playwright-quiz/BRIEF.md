# Session Playwright — Application de quiz

## Contexte

Une app de quiz à choix multiples est déjà construite. Elle contient 3 questions, chacune avec 4 réponses possibles. L'utilisateur navigue de question en question, puis voit son score final. Les tests E2E sont fournis mais échouent — tu dois implémenter les Page Objects.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://127.0.0.1:5001
```

## Ce que tu dois tester

Le parcours d'un utilisateur qui passe le quiz :
- Voir la première question affichée correctement
- Sélectionner une réponse et passer à la suivante
- Arriver sur la page de résultat avec le bon score
- Recommencer le quiz depuis la page de résultat

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Le bouton change de texte à la dernière question ("Voir le score" au lieu de "Suivant")

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas `tests/`
- Inspecte `app/templates/` pour comprendre le DOM
