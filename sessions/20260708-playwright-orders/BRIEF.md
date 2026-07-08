# Session Playwright — Tableau de bord de commandes

## Contexte

Une app de suivi de commandes est déjà construite. Elle affiche 5 commandes avec leurs statuts (en attente, expédiée, livrée). Tu peux filtrer par statut et modifier le statut de chaque commande. Des compteurs en haut de page indiquent le nombre de commandes par statut.

## Lancer le serveur

```bash
cd app && python3 server.py
# App disponible sur http://127.0.0.1:5001
```

## Ce que tu dois tester

Le parcours d'un gestionnaire de commandes :
- Voir toutes les commandes au chargement
- Filtrer la liste par statut
- Modifier le statut d'une commande et vérifier la mise à jour
- Vérifier que les compteurs en haut de page reflètent la réalité

## Critères d'acceptance

- [ ] Tous les tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires couvrant des cas non testés
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role` — pas de CSS fragile)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] Les compteurs de statut sont vérifiés dans au moins un test

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais pas `tests/`
- Inspecte `app/templates/orders.html` pour comprendre le DOM
