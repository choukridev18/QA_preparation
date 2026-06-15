# Session Playwright — Formulaire multi-étapes

## Contexte

Une app Flask d'inscription en 3 étapes est déjà construite. L'utilisateur remplit ses informations personnelles (étape 1), choisit un plan (étape 2), puis confirme son inscription (étape 3). Les Page Objects sont des stubs — toutes les méthodes lèvent `NotImplementedError`. Tu dois les implémenter pour que les 6 tests fournis passent.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

- Étape 1 : prénom vide → erreur, email invalide → erreur, formulaire valide → étape 2
- Étape 2 : sans plan → erreur, bouton "Retour" → retour étape 1
- Parcours complet → page de succès avec les bonnes données en confirmation

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`)
- [ ] Pas de `time.sleep()`
- [ ] Le POM encapsule toute l'interaction

## Contraintes

- Playwright Python — sync API uniquement
- Trois classes POM : `Step1Page`, `Step2Page`, `ConfirmPage`
- Tu peux modifier `pages/` mais **pas** `tests/`
- Inspecte `app/templates/` pour les sélecteurs

## Indices HTML utiles

| Élément                      | Sélecteur                                          |
|-----------------------------|----------------------------------------------------|
| Champ Prénom                | `get_by_label("Prénom")`                           |
| Champ Nom                   | `get_by_label("Nom")`                              |
| Champ Email                 | `get_by_label("Email")`                            |
| Bouton Suivant              | `get_by_role("button", name="Suivant")`            |
| Lien Retour (étape 2)       | `get_by_role("link", name="Retour")`               |
| Select Plan                 | `get_by_label("Plan")`                             |
| Erreur prénom               | `#error-first-name`                                |
| Erreur email                | `#error-email`                                     |
| Erreur plan                 | `#error-plan`                                      |
| Récap prénom (confirmation) | `#summary-first-name`                              |
| Récap plan (confirmation)   | `#summary-plan`                                    |
| Bouton confirmer            | `get_by_role("button", name="Confirmer l'inscription")` |
