# Liste complète des bugs

<details>
<summary>⚠️ Spoiler — à lire seulement après avoir fini (ou abandonné)</summary>

## Bug 1 — `tests/test_weather_client.py`, `test_get_temperature_city_name`

**Symptôme :** `AssertionError: assert 'Paris' == 'paris'`  
**Cause :** La casse est incorrecte dans l'assertion. L'API retourne `"Paris"` (majuscule), le test compare avec `"paris"`.  
**Correction :** `assert result["city"] == "Paris"`

---

## Bug 2 — `tests/test_weather_client.py`, `test_get_temperature_empty_city`

**Symptôme :** `ValueError: Le nom de la ville ne peut pas être vide` (l'exception se propage hors du bloc `pytest.raises`)  
**Cause :** Le test attend `ConnectionError` mais `get_temperature("")` lève `ValueError`. Le type d'exception est incorrect.  
**Correction :** `with pytest.raises(ValueError):`

---

## Bug 3 — `tests/test_weather_client.py`, `test_get_temperature_server_error`

**Symptôme :** `Failed: DID NOT RAISE <class 'ConnectionError'>`  
**Cause :** Le mock est configuré **après** l'appel à `client.get_temperature("Paris")`. Au moment de l'appel, `mock_get.return_value.status_code` n'est pas encore `500` — c'est un `MagicMock`, donc `response.status_code == 500` est `False` et `ConnectionError` n'est jamais levée.  
**Correction :** déplacer `mock_get.return_value.status_code = 500` **avant** l'entrée dans `pytest.raises` :

```python
def test_get_temperature_server_error(client):
    with patch("src.weather_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        with pytest.raises(ConnectionError):
            client.get_temperature("Paris")
```

---

## Bug 4 — `tests/test_weather_client.py`, `test_get_forecast_returns_sorted_conditions`

**Symptôme :** `TypeError: 'dict' object is not callable`  
**Cause :** `mock_response.json` est remplacé directement par un `dict`. Quand le code fait `response.json()`, il appelle le dict comme une fonction → `TypeError`. Il faut que `json` reste un `MagicMock` et que la valeur de retour soit configurée via `.return_value`.  
**Correction :**

```python
mock_response.json.return_value = {"conditions": ["nuageux", "ensoleillé", "pluvieux"]}
```

---

## Bug 5 — `tests/test_weather_client.py`, `test_get_forecast_unsorted_input`

**Symptôme :** `AssertionError: assert ['brumeux', 'ensoleillé', 'venteux'] == ['venteux', 'ensoleillé', 'brumeux']`  
**Cause :** `get_forecast` retourne une liste **triée alphabétiquement** (c'est sa responsabilité documentée). L'assertion compare avec la liste dans l'ordre d'entrée non trié.  
**Correction :** `assert result == ["brumeux", "ensoleillé", "venteux"]`

</details>
