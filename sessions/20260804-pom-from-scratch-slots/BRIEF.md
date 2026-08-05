# Réservation de créneaux — From scratch

## Contexte
Une application de réservation de créneaux horaires. L'utilisateur choisit un créneau parmi une liste, le confirme, et peut l'annuler. Un créneau déjà réservé par quelqu'un d'autre n'est plus disponible. Un utilisateur ne peut avoir qu'une seule réservation active à la fois.

## Lancer le serveur

```bash
cd app
python server.py
```

Port : **5001**

## Critères d'acceptation (5 tests minimum)

- [ ] Réserver un créneau valide → redirige vers la page de confirmation avec le bon label
- [ ] Réserver un créneau déjà pris → message d'erreur affiché
- [ ] Réserver deux fois (même session) → message d'erreur affiché
- [ ] Annuler sa réservation → retour à la liste, créneau à nouveau disponible
- [ ] Soumettre sans sélectionner de créneau → message d'erreur affiché

## Contraintes

- POM obligatoire dans `pages/` — une classe par page
- API **sync** Playwright uniquement
- Pas de `time.sleep()`
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator` avec `id`
- Assertions d'URL avec `expect(page).to_have_url(...)`
- Ouvre `app/templates/` pour construire ton POM avant d'écrire les tests
