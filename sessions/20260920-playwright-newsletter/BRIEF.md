# Session Playwright — Préférences newsletter

## Contexte

Mini app Flask de gestion des préférences d'une newsletter : email, catégories (checkboxes), fréquence (radios).  
Les préférences sont stockées en mémoire. Un enregistrement valide affiche un message de succès et un résumé.  
Les cas invalides (email manquant, aucune catégorie) affichent une alerte.

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://127.0.0.1:5001
```

## Ce que tu dois tester

Un utilisateur arrive sur `/preferences`, remplit ses choix, et enregistre.  
Tu dois couvrir le parcours heureux et les erreurs de validation du formulaire.

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Au moins un test supplémentaire passe par la page `/summary` après un enregistrement réussi

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas les tests fournis dans `tests/test_newsletter.py`
- Tu peux ajouter de nouveaux fichiers de tests
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Idées de tests supplémentaires

- Email invalide (sans `@`) → erreur
- Enregistrement puis navigation vers `/summary` → données cohérentes
- Fréquence manquante → erreur
- Plusieurs catégories cochées apparaissent toutes dans le résumé
