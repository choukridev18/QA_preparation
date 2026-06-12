# Session Playwright — Interface de support

## Contexte

Une app Flask de gestion de tickets de support est déjà construite. Les utilisateurs peuvent soumettre des tickets (titre, catégorie, description), consulter la liste, et marquer un ticket comme résolu. Les Page Objects sont des stubs — toutes les méthodes lèvent `NotImplementedError`. Tu dois les implémenter pour que les 6 tests fournis passent.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

- Consulter la liste des tickets (titres affichés, compteur ouvert)
- Naviguer vers le formulaire de création
- Soumettre un ticket valide → il apparaît dans la liste
- Soumettre sans titre → erreur inline
- Cliquer "Résolu" → statut mis à jour

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Les méthodes `get_*` lisent l'état, les méthodes `fill_*` / `select_*` / `submit` agissent

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire — deux classes : `TicketListPage` et `NewTicketPage`
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Indices HTML utiles

| Élément                        | Sélecteur à utiliser                                  |
|-------------------------------|-------------------------------------------------------|
| Compteur tickets ouverts       | `#open-count-number`                                  |
| Titres des tickets             | `.ticket-title`                                       |
| Statut d'un ticket (par ID)    | `#ticket-1 .ticket-status`                            |
| Bouton "Résolu" (par ID)       | `get_by_role("button", name="Résoudre le ticket 1")`  |
| Lien "Nouveau ticket"          | `get_by_role("link", name="Nouveau ticket")`          |
| Champ Titre (formulaire)       | `get_by_label("Titre")`                               |
| Select Catégorie               | `get_by_label("Catégorie")`                           |
| Champ Description              | `get_by_label("Description")`                         |
| Bouton Soumettre               | `get_by_role("button", name="Soumettre")`             |
| Erreur titre                   | `#error-title`                                        |
| Erreur catégorie               | `#error-category`                                     |
