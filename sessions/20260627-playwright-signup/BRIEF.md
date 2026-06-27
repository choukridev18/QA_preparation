# Session Playwright — Formulaire d'inscription 2 étapes

## Contexte

Une app d'inscription en 2 étapes est déjà construite. L'étape 1 collecte les informations personnelles (nom, email, mot de passe). L'étape 2 collecte les préférences (newsletter, langue). Une page de confirmation s'affiche après l'inscription. Les tests E2E sont fournis mais échouent — tu dois implémenter les Page Objects.

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://127.0.0.1:5001
```

## Ce que tu dois tester

Le parcours d'un utilisateur qui crée un compte :
- Remplir ses informations personnelles à l'étape 1
- Passer à l'étape 2 pour ses préférences
- Finaliser l'inscription et arriver sur la page de confirmation
- Voir les messages d'erreur si les données sont invalides
- Pouvoir revenir à l'étape 1 depuis l'étape 2

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] La page de confirmation affiche bien le nom de l'utilisateur

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas `tests/`
- Inspecte `app/templates/` pour comprendre le DOM (pas besoin d'ouvrir le navigateur)
