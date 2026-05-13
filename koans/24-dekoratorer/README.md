# 24 — Dekoratorer

> `@decorator` är socker för `f = decorator(f)` — en dekoratör är en funktion som tar en funktion och returnerar en funktion.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att `@decorator` är syntaktisk socker och vad det expanderar till
- Varför `functools.wraps` behövs och vad som händer med `__name__` utan det
- Hur en dekoratör med argument (`@repeat(3)`) är strukturerad som en fabriksdekoratör
- I vilken ordning staplade dekoratorer appliceras

## Komma igång

```bash
uv run pytest koans/24-dekoratorer/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Staplade dekoratorer: `@A @B def f` → `f = A(B(f))` — B appliceras innerst
- `functools.cache` är en dekoratör för memoization

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad expanderar `@min_dekorator\ndef f(): ...` till? Skriv ut det utan `@`-syntax.
- Vad händer med `f.__name__` utan `functools.wraps`? Varför spelar det roll?
- Om `@A @B def f:` — vilken dekoratör appliceras närmast `f`? I vilken ordning anropas de vid ett anrop av `f()`?
