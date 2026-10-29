# Brief — Accès interne

## Contexte

Portail RH minimal : une page **connexion**, puis un **espace membre** après authentification.
Compte de démo pour les tests : **employe@interne.fr** / **qa-demo**.

Pas d'inscription ni de mot de passe oublié.

## Lancer le serveur

```bash
cd app
python3 server.py
```

Serveur : http://127.0.0.1:5001

## Critères d'acceptation (minimum 4 tests)

1. La page de connexion affiche les champs email et mot de passe et le bouton de connexion.
2. Des identifiants incorrects affichent un message d'erreur (sans accéder à l'espace membre).
3. Des identifiants corrects ouvrent l'espace membre avec un message de bienvenue contenant l'email.
4. Un accès direct à l'espace membre **sans** être connecté renvoie vers la page de connexion.
5. (Bonus) La déconnexion ramène à la page de connexion.

## Contraintes

- POM obligatoire : **une classe par écran principal** (connexion + espace membre).
- API sync Playwright uniquement.
- Pas de `time.sleep()`.
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator`.
- Assertions : `expect` pour l'état visible / URL ; `assert` pour textes ciblés si besoin.

## Structure à créer

```
pages/
└── (tes classes POM)

tests/
└── (tes test_*.py)

conftest.py
└── reset + fixtures connexion / espace membre si tu en as besoin
```

Ouvre `app/templates/` avant d'écrire le POM.
