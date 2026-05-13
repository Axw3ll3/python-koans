# 17 — Kontexthanterare

> `with` garanterar att `__exit__` anropas — även om ett undantag kastas inuti blocket.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vad `with`-satsen garanterar och varför det är viktigt för resurser som filer och databasanslutningar
- Att `__exit__` anropas oavsett om ett undantag kastades
- Vad koden *efter* `yield` i `@contextlib.contextmanager` gör
- Ordningen för `__exit__` vid kapslade kontexthanterare

## Komma igång

```bash
uv run pytest koans/17-kontexthanterare/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "with open('/dev/null') as f: print(f.closed); print(f.closed)"`
- Koden efter `yield` i en `@contextmanager`-funktion är cleanup-koden — den körs när `with`-blocket avslutas

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer med filen om ett undantag kastas inuti ett `with open(...) as f:`-block?
- I `@contextlib.contextmanager`: vad är koden *före* `yield` respektive koden *efter* `yield`?
- Vad gör det att `__exit__` returnerar `True`? Vad händer med undantaget?
