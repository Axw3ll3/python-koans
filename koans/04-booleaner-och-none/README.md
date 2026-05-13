# 04 — Booleaner och None

> Python utvärderar alla objekt som sant eller falskt — och `and`/`or` returnerar operanderna, inte True/False.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vilka värden som är falsy: `None`, `0`, `""`, `[]`, `{}`, `set()`, `()`
- Att `and` och `or` returnerar en av operanderna, inte ett booleskt värde
- Varför `is None` är att föredra framför `== None`
- Hur kortslutningsutvärdering fungerar

## Komma igång

```bash
uv run pytest koans/04-booleaner-och-none/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "print('hej' or 'standard', '' or 'standard')"`
- `and` returnerar det första falsy värdet, eller det sista om alla är truthy

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad returnerar `"" or "standard"`? Varför — vad är mekanismen bakom `or`?
- Vad är skillnaden mellan `x == None` och `x is None`? Varför rekommenderar Python `is None`?
- Vad returnerar `None and "hej"`? Förklara kortslutning steg för steg.
