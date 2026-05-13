# 20 — Dunder-metoder

> Duck typing: Python bryr sig inte om klassen — bara om att objektet implementerar rätt protokoll.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att inbyggda operatorer (`len`, `+`, `in`, `[]`, `bool`) anropar specifika dunder-metoder
- Varför implementering av `__eq__` automatiskt sätter `__hash__` till None
- Att `__iter__` + `__next__` implementerar iterator-protokollet
- Vad duck typing innebär i praktiken

## Komma igång

```bash
uv run pytest koans/20-dunder-metoder/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "class A:\n    def __len__(self): return 42\nprint(len(A()))"`
- `__call__` gör en instans anropbar: `obj()` anropar `obj.__call__()`

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer med `__hash__` när du implementerar `__eq__`? Varför är det ett problem?
- Vad krävs för att en klass ska följa iterator-protokollet och kunna användas i `for`?
- Vad betyder "duck typing"? Ge ett konkret exempel på hur det skiljer sig från statisk typning.
