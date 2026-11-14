# Brief — Ticket support

## Contexte

Portail support interne sur **une seule page** : formulaire (sujet, priorité, description) et liste des tickets créés.
Après création, un message de succès s'affiche et le ticket apparaît dans la liste.
Pas de connexion ni de deuxième page.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 4 tests)

1. La page affiche les champs sujet, priorité, description et le bouton de création.
2. Après création d'un ticket, un message de succès est visible.
3. Le sujet du ticket créé apparaît dans la liste.
4. Après reset (ou avant tout ticket), la liste est vide avec le message d'état prévu.
5. (Bonus) La priorité choisie est visible sur la ligne du ticket.

## Contraintes

- POM obligatoire : **une classe** pour cet écran.
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions : `expect` pour visibilité / URL ; `assert` pour textes et comptes si besoin.

## Structure à créer

```
pages/
└── (ta classe POM)

tests/
└── (tes test_*.py)

conftest.py
└── reset + fixture page support si tu en as besoin
```

Ouvre `app/templates/` avant d'écrire le POM.