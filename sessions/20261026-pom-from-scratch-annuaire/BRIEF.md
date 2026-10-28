# Brief — Annuaire

## Contexte

L'entreprise a un petit annuaire interne. On tape un nom (ou un bout de nom), on voit les collègues qui correspondent.
Sans recherche, la liste complète s'affiche. Si rien ne correspond, un message l'indique.
Il n'y a pas de connexion ni de deuxième page.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur disponible sur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 4 tests)

1. Sans recherche, la liste affiche tous les collègues.
2. Une recherche qui matche un nom affiche ce collègue.
3. Une recherche ne montre pas les collègues qui ne correspondent pas.
4. Une recherche sans résultat affiche le message d'état vide.
5. (Bonus) La recherche ne tient pas compte des majuscules / minuscules.

## Contraintes

- POM obligatoire : une classe pour cet écran.
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions avec `expect` pour l'état visible, `assert` pour les textes / comptes Python.

## Structure à créer

```
pages/
└── (ta classe POM)

tests/
└── (tes test_*.py)

conftest.py
└── tu ajoutes tes fixtures (reset, page annuaire, etc.)
```

Ouvre `app/templates/` avant d'écrire le POM.
