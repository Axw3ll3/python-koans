# 09 — Kontrollflöde

> Python-jämförelser kan kedjas — `1 < x < 10` är inte ett hack, det är idiomatisk Python.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Hur det ternära uttrycket `x if villkor else y` utvärderas
- Varför `1 < 2 > 3` är False (inte ett fel)
- Vad `pass` gör och varför det behövs
- Hur `match`/`case` (Python 3.10+) skiljer sig från kedjad `if`/`elif`

## Komma igång

```bash
uv run pytest koans/09-kontrollflode/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "print(1 < 2 > 3)"`
- `x if villkor else y` returnerar `x` om villkoret är sant, annars `y`

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Hur utvärderar Python `1 < 2 > 3`? Vilka jämförelser görs och i vilken ordning?
- Vad är skillnaden mellan `not x in lst` och `x not in lst`? Är de ekvivalenta?
- Vad returnerar `"stor" if x % 2 == 0 else "liten"` när `x = 5`? Förklara utvärderingen.
