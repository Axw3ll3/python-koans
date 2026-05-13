# 06 — Tupler

> Ett enda kommatecken avgör om du har en tupel eller ett parentesuttryck — `(42)` är ett heltal, `(42,)` är en tupel.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Varför `(42,)` är en tupel men `(42)` är ett heltal
- Hur tupeluppackning (destructuring) fungerar
- Varför tupler kan användas som dict-nycklar när listor inte kan
- Pythons idiomatiska swap: `a, b = b, a`

## Komma igång

```bash
uv run pytest koans/06-tupler/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "print(type((42)), type((42,)))"`
- Det är kommatecknet, inte parentesen, som gör en tupel

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför är `(42)` ett heltal och inte en tupel? Vad är det som skapar en tupel?
- Varför kan tupler användas som dict-nycklar men inte listor? Vad är kravet för att vara hashbar?
- Vad händer steg för steg när Python utvärderar `a, b = b, a`?
