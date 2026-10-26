# Brief — Demande de congés

## Contexte

Les salariés déposent une demande de congés : dates + motif.
Si tout est bon, ils arrivent sur une page de confirmation qui rappelle les infos.
Si un champ manque ou que les dates sont incohérentes, ils restent sur le formulaire avec une erreur.
Sans demande envoyée, la page de confirmation n'est pas accessible.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur disponible sur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 4 tests)

1. Une demande complète affiche la page de confirmation (URL + titre).
2. Les dates et le motif saisis apparaissent sur la confirmation.
3. Un champ manquant affiche un message d'erreur, sans quitter le formulaire.
4. Une date de fin avant la date de début affiche l'erreur correspondante.
5. (Bonus) Ouvrir `/confirmation` sans avoir envoyé de demande ramène au formulaire.

## Contraintes

- POM obligatoire : **une classe par écran** (formulaire et confirmation).
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions avec `expect` pour l'URL / l'état visible, `assert` pour les textes Python.

## Structure à créer

```
pages/
└── (tes classes POM)

tests/
└── (tes test_*.py)

conftest.py
└── tu ajoutes tes fixtures (reset, page formulaire, etc.)
```

Ouvre `app/templates/` avant d'écrire le POM.
