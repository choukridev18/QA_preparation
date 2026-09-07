# Brief — Formulaire de candidature

## Contexte

Une startup utilise un formulaire de candidature en ligne en 2 étapes.
L'étape 1 collecte les informations personnelles du candidat.
L'étape 2 collecte le poste visé, l'expérience et la lettre de motivation.
Une page de confirmation s'affiche si tout est valide.

## Lancer le serveur

```bash
cd app
python server.py
```

Serveur disponible sur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 5 tests)

1. Un formulaire valide à l'étape 1 redirige vers l'étape 2.
2. Soumettre l'étape 1 sans nom affiche un message d'erreur.
3. Soumettre l'étape 1 avec un email invalide (sans @) affiche un message d'erreur.
4. Un formulaire valide à l'étape 2 redirige vers la page de confirmation.
5. La page de confirmation affiche le nom et le poste du candidat.
6. (Bonus) Soumettre l'étape 2 avec une motivation trop courte affiche un message d'erreur.
7. (Bonus) Accéder directement à l'étape 2 sans avoir complété l'étape 1 redirige vers l'étape 1.

## Contraintes

- POM obligatoire : une classe par écran.
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_label`, `get_by_role`, `locator`.
- Assertions avec `expect` pour les URLs et états visibles.

## Structure à créer

```
pages/
└── candidature_page.py   ← tes classes POM

tests/
└── test_candidature.py   ← tes tests
```

Ouvre `app/templates/` pour identifier les locators avant d'écrire le POM.
