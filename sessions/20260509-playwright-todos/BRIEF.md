# Session Playwright — Gestionnaire de tâches

## Contexte

L'app est un gestionnaire de todos avec ajout, marquage comme terminé, suppression
et filtrage par statut. Elle est déjà construite. Ton travail : implémenter le Page Object
`pages/todos_page.py` (7 TODOs) pour faire passer les 3 tests fournis, puis écrire
au moins 2 tests supplémentaires.

## Lancer le serveur

```bash
cd app && python server.py
# App disponible sur http://localhost:5001
```

## Ce que tu dois tester

Un utilisateur crée des tâches, en marque certaines comme terminées, en supprime d'autres,
et filtre la liste pour voir uniquement les actives ou les terminées.

## Critères d'acceptance

- [ ] Les 3 tests fournis passent
- [ ] Tu as ajouté au moins 2 tests supplémentaires
- [ ] Tes locators sont sémantiques (`get_by_label`, `get_by_role`, `get_by_text`)
- [ ] Pas de `time.sleep()` — utilise `expect()` ou `wait_for_*`
- [ ] Le POM encapsule toute l'interaction — les tests n'appellent pas Playwright directement
- [ ] `set_filter` utilise le texte visible du lien ("Actives", "Terminées", "Toutes")

## Contraintes

- Playwright Python — sync API uniquement
- Page Object Model obligatoire
- Tu peux modifier `pages/` mais **pas** `tests/`
- Tu peux inspecter `app/templates/` pour comprendre le DOM

## Idées pour les tests supplémentaires

- Ajouter 2 tâches, en terminer une, filtrer "Terminées" → vérifier qu'il y en a 1
- Ajouter 3 tâches, en supprimer une → vérifier qu'il en reste 2
- Vérifier que le filtre "Toutes" reaffiche tout après un filtre "Actives"
- Vérifier que naviguer sur `/` sans rien ajouter affiche le message vide
