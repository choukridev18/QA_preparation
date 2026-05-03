# Programme de formation QA Automation

## Règles générales

- **7 jours sur 7** — chaque jour a une session définie, pas de repos, pas de libre
- Chaque session génère ses propres fichiers — tu codes dans le dossier créé par l'agent
- Pas d'enregistrement oral, pas d'anglais — tu te concentres sur le code et les tests
- Après chaque session, lis le débrief : c'est là que la progression se construit

---

## Semaine type

### Lundi — Drill Python pur

> Session langage complète. 45-60 minutes pour travailler les fondamentaux Python en profondeur.

1. Lance `/qa-python-lang` — l'agent propose 3 thèmes, tu choisis
2. Implémente les fonctions dans `exercise.py` (5 à 7 fonctions)
3. Lance `python exercise.py` jusqu'à voir `✅ Tous les tests passent.`
4. Lis le feedback court de l'agent

**Objectif de progression :**

- Semaines 1-2 : arriver au résultat même en consultant la doc Python
- Semaines 3+ : utiliser les bons outils du premier coup (compréhensions, `sorted(key=)`, `@dataclass`…) sans chercher

---

### Mardi — Session Playwright complète

> Le cœur de la formation. Tu arrives sur une codebase inconnue et tu dois tester un parcours utilisateur.

1. Lance `/qa-playwright-session` — l'agent propose 3 scénarios, tu choisis
2. Explore la structure générée (POM stubs, conftest, brief)
3. Implémente les méthodes du Page Object + les tests
4. Écris au moins 2 tests supplémentaires qui ne sont pas dans le brief
5. Dis "j'ai fini" pour déclencher le débrief

**Objectif de progression :**

- Semaines 1-2 : faire passer les tests fournis
- Semaines 3+ : écrire des tests stables (locators sémantiques, pas de CSS fragile) + couvrir les cas aux limites

---

### Mercredi — Chasse aux bugs

> Tu récupères une suite de tests qui était verte. Elle ne l'est plus. Trouve pourquoi.

1. Lance `/qa-bug-hunt` — l'agent propose 3 scénarios de bugs, tu choisis
2. Lance `pytest` et analyse les erreurs
3. Trouve et corrige tous les bugs dans les fichiers de tests
4. Dis "j'ai fini" pour que l'agent révèle la liste complète et fasse le débrief

**Objectif de progression :**

- Semaines 1-2 : trouver les bugs évidents (mauvaise assertion, mauvais sélecteur)
- Semaines 3+ : détecter les bugs subtils (mauvais scope de fixture, mock mal ciblé, condition de course)

---

### Jeudi — Session Playwright complète

> 2ème session E2E de la semaine. L'agent génère un scénario différent du mardi.

Même workflow que mardi. L'agent évite automatiquement de répéter un scénario récent.

---

### Vendredi — Drill Python/pytest

> Session testing complète. 45-60 minutes pour ancrer les réflexes pytest de la semaine.

1. Lance `/qa-python-drill` — l'agent propose 3 thèmes, tu choisis
2. Implémente les fonctions dans `exercise.py` (5 à 7 fonctions)
3. Lance `pytest test_exercise.py -v` jusqu'à ce que tous les tests passent
4. Lis le feedback court de l'agent

**Objectif de progression :**

- Semaines 1-2 : faire passer tous les tests même si c'est pas élégant
- Semaines 3+ : utiliser `parametrize`, les fixtures et les mocks sans chercher la doc à chaque fois

---

### Samedi — Chasse aux bugs

> 2ème session de bug hunt de la semaine. L'agent génère un scénario différent du mercredi.

Même workflow que mercredi. L'agent évite automatiquement de répéter un scénario récent.

---

### Dimanche — Session Playwright complète

> 3ème session E2E de la semaine — souvent la plus ambitieuse car le week-end donne plus de temps.

Même workflow que mardi et jeudi. L'agent génère un scénario différent des deux autres sessions de la semaine.

---

## Récap hebdomadaire


| Jour     | Skill                    | Durée   |
| -------- | ------------------------ | ------- |
| Lundi    | `/qa-python-lang`        | ~1h     |
| Mardi    | `/qa-playwright-session` | ~1h     |
| Mercredi | `/qa-bug-hunt`           | ~40 min |
| Jeudi    | `/qa-playwright-session` | ~1h     |
| Vendredi | `/qa-python-drill`       | ~1h     |
| Samedi   | `/qa-bug-hunt`           | ~40 min |
| Dimanche | `/qa-playwright-session` | ~1h     |


**Total : ~6h20/semaine**

Répartition : 3× Playwright · 2× Bug hunt · 1× Python pur · 1× Python/pytest

### Session optionnelle — POM & tests from scratch

> **Pas** dans le total hebdo ci-dessus. À faire **de temps en temps** (idéalement **1× / semaine** ou **1× / 2 semaines**), entre deux jours Playwright lourds — par ex. un **mercredi soir**, **jeudi matin**, ou **lundi / vendredi** si tu veux consolider sans recopier des stubs.

1. Lance `/qa-playwright-from-scratch` — l’agent propose 3 scénarios, tu choisis.
2. L’agent génère **l’app Flask + le brief** ; les dossiers **`pages/`** et **`tests/`** restent **vides** : tu crées **toi-même** tous les Page Objects et **tous** les tests.
3. Tu respectes la checklist du **`BRIEF.md`** (nombre de tests, parcours à couvrir).
4. Dis « j’ai fini » pour le débrief.

**Objectif** : ne plus dépendre des TODO pré-remplis des sessions `/qa-playwright-session`.

---

## Signaux de progression

Tu es opérationnel en QA Automation quand :

- **Python pur** : tu manipules des listes, dicts, dataclasses et classes sans chercher la doc à chaque fois
- **Drill pytest** : tu choisis `parametrize`, les fixtures et les mocks sans hésiter
- **Playwright** : tes locators sont sémantiques (`get_by_role`, `get_by_label`), tes tests sont stables au re-run, tu as un POM propre dès la première fois
- **Bug hunt** : tu lis un traceback pytest et tu identifies le type de bug en moins de 2 minutes sans toucher au code de prod
- **Global** : tu arrives sur un projet inconnu, tu comprends la structure des tests existants et tu sais où ajouter les tiens