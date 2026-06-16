# Solutions — Bug Hunt : Client météo mocké

<details>
<summary>🔴 Bug 1 — test_get_forecast_returns_dict</summary>

**Problème :** chemin du patch incorrect.
`mock.patch("weather.requests.get", ...)` → le module `weather` n'existe pas.

**Correction :**
```python
with mock.patch("src.weather.requests.get", return_value=mock_response):
```
</details>

<details>
<summary>🔴 Bug 2 — test_get_forecast_raises_on_error</summary>

**Problème :** mauvais type d'exception attendu.
`pytest.raises(ValueError)` → la fonction lève `WeatherError` (sous-classe de `RuntimeError`, pas de `ValueError`).

**Correction :**
```python
with pytest.raises(WeatherError):
```
</details>

<details>
<summary>🔴 Bug 3 — test_send_alert_returns_true_on_success</summary>

**Problème :** l'assertion est inversée.
`assert result is False` → la fonction retourne `True` quand le status est 200.

**Correction :**
```python
assert result is True
```
</details>

<details>
<summary>🔴 Bug 4 — test_get_temperature_calls_get_forecast</summary>

**Problème :** `return_value = None` fait planter `get_temperature` car elle accède à `forecast["temp"]`.
Le mock doit retourner un dict valide.

**Correction :**
```python
mock_fc.return_value = {"city": "Bordeaux", "temp": 25.0, "condition": "Soleil"}
temp = get_temperature("Bordeaux")
assert temp == 25.0
```
</details>

<details>
<summary>🔴 Bug 5 — test_format_forecast_hot_city</summary>

**Problème :** la température `38.0` est un float, donc Python affiche `38.0°C`, pas `38°C`.

**Correction :**
```python
assert result == "Séville : Très chaud, 38.0°C"
```
</details>
