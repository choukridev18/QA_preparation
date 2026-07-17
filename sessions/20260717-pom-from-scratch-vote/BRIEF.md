# Sondage / Vote — From scratch

## Contexte
Une application de sondage simple. L'utilisateur vote pour son langage de programmation préféré parmi 4 options (Python, JavaScript, Java, Go). Il ne peut voter qu'une seule fois par session. La page résultats affiche le nombre de votes et le pourcentage pour chaque option.

## Lancer le serveur

```bash
cd app
python server.py
```

Port : **5001**

## Critères d'acceptation (5 tests minimum)

- [ ] Voter pour une option valide → redirige vers `/results`
- [ ] Voter deux fois → message d'erreur affiché sur la page de vote
- [ ] Soumettre sans sélectionner d'option → message d'erreur affiché
- [ ] Après un vote, la page résultats affiche le bon total (1 vote)
- [ ] Le lien "Voter à nouveau" ramène sur la page de vote (URL `/`)

## Contraintes

- POM obligatoire dans `pages/` — une classe par page
- API **sync** Playwright uniquement
- Pas de `time.sleep()`
- Locators sémantiques : `get_by_role`, `get_by_label`, `locator` avec `id` ou `class`
- Assertions d'URL avec `expect(page).to_have_url(...)`
- Ouvre `app/templates/` pour construire ton POM avant d'écrire les tests
