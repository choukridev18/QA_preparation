# Session Playwright — Formulaire de réservation multi-étapes

## Contexte

L'app est un formulaire de réservation en 3 étapes : informations personnelles (étape 1), détails de la réservation (étape 2), puis récapitulatif et confirmation (étape 3). Elle est déjà construite. Ton travail : implémenter le Page Object `pages/booking_page.py` (9 TODOs) pour faire passer les 3 tests fournis, puis écrire au moins 2 tests supplémentaires.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Un utilisateur remplit ses informations personnelles, choisit une date et un nombre de personnes, vérifie le récapitulatif, puis confirme sa réservation. En cas d'erreur (champ vide, email invalide), un message s'affiche et l'utilisateur reste sur la même étape.

## Critères d'acceptance

- [ ] Les 3 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`, `get_by_text`)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] `get_error_message()` retourne `""` si aucun message n'est visible

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Idées pour les tests supplémentaires

- Soumettre l'étape 1 avec un email sans `@` → erreur visible
- Soumettre l'étape 2 sans date → erreur visible
- Accéder directement à `/step2` sans passer par l'étape 1 → redirection vers `/step1`
- Vérifier que la date saisie apparaît dans le récapitulatif
