# Bug Hunt — Client météo mocké

## Contexte

Tu as reçu un module `src/weather.py` — un wrapper autour d'une API météo externe.
Le code de production est **correct**. Les tests, eux, contiennent **5 bugs** à corriger.

Ton rôle : trouver et corriger les tests sans toucher à `src/weather.py`.

---

## Structure

```
hunts/20260616-hunt-weather/
├── src/
│   └── weather.py          ← code de production (ne pas modifier)
├── tests/
│   ├── conftest.py         ← fixtures (ne pas modifier)
│   └── test_weather.py     ← 5 bugs à corriger ici
└── requirements.txt
```

---

## Lancer les tests

```bash
cd hunts/20260616-hunt-weather
python -m pytest tests/ -v
```

Tu dois voir **3 tests passer** et **5 tests échouer** au départ.

---

## Fonctions testées

| Fonction | Description |
|---|---|
| `get_forecast(city)` | Appelle l'API, retourne un dict, lève `WeatherError` si erreur |
| `format_forecast(forecast)` | Formate le dict en chaîne lisible |
| `send_alert(city, message)` | POST sur l'API d'alertes, retourne True/False |
| `get_temperature(city)` | Retourne uniquement la température |
| `is_alert_needed(temp, threshold)` | Retourne True si temp ≥ seuil |

---

## Indices (si tu bloques)

<details>
<summary>Indice général</summary>
Concentre-toi sur : le chemin du patch, le type d'exception attendu, la valeur retournée, le retour de `return_value`, et le format de la chaîne.
</details>
