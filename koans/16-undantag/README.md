# 16 — Undantag

> `finally` körs alltid — även om det finns ett `return` i `try`-blocket.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vad `else` i ett `try`-block gör (körs om inget undantag kastades)
- Att `finally` körs oavsett om ett undantag kastades eller inte — även vid `return`
- Skillnaden mellan att fånga `Exception` och `BaseException`
- Vad naken `raise` (utan argument) gör i ett `except`-block

## Komma igång

```bash
uv run pytest koans/16-undantag/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- `SystemExit` och `KeyboardInterrupt` ärver från `BaseException`, inte `Exception`
- Naken `raise` i ett `except`-block kastar om *samma* undantag med *originalstacktrace*

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Under vilket villkor körs `else`-blocket i `try`/`except`/`else`/`finally`?
- Vad gör `raise` utan argument i ett `except`-block? Varför är det användbart?
- Varför fångar `except Exception` inte `SystemExit`? Vad ärver `SystemExit` från?
