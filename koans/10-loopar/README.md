# 10 — Loopar

> `for`/`else` är Pythons djärvaste konstrukt — `else`-blocket körs bara om loopen *inte* bröts av `break`.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att `for` itererar över alla iterables, inte bara listor och ranges
- Vad loopvariabeln håller för värde *efter* att en `for`-loop är klar
- Varför `for`/`else` inte fungerar som `if`/`else`
- Hur `enumerate` och `zip` fungerar och vad de returnerar

## Komma igång

```bash
uv run pytest koans/10-loopar/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "for i in range(3): pass; print(i)"`
- `zip` stannar vid den kortaste sekvensen — det är inte ett fel

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Under vilket villkor körs `else`-blocket i en `for`/`else`-loop?
- Vad är värdet av loopvariabeln `i` efter att `for i in range(5): pass` har körts?
- Vad returnerar `list(zip([1, 2, 3], ["a", "b"]))` och varför har resultatet bara två element?
