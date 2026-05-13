# 03 — Strängar

> Strängar är immutabla sekvenser — du kan inte ändra dem, bara skapa nya.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Varför `s[0] = "H"` kastar ett undantag för en sträng
- Hur indexering och slicning fungerar (inklusive negativa index)
- Att strängmetoder som `.lower()` och `.replace()` returnerar nya strängar — originalet ändras inte
- Hur f-strängar formateras

## Komma igång

```bash
uv run pytest koans/03-strangar/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "s = 'hej'; print(s.upper()); print(s)"`
- Negativa index räknar från slutet: `s[-1]` är sista tecknet

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer med originalet `s` om du anropar `s.upper()`? Varför?
- Vad är skillnaden mellan `"a" + "b"` och `"".join(["a", "b"])`? När är `join` att föredra?
- Vad returnerar `"python"[-3:]`? Förklara hur negativ slicning fungerar.
