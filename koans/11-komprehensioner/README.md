# 11 — Komprehensioner

> `[x for x in range(3)]` är en lista. `(x for x in range(3))` är en generator — same syntax, fundamentalt annorlunda beteende.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Skillnaden mellan listkomp (skapar lista) och generatoruttryck (lat iterable)
- Hur filtret `if` i en komprehension fungerar
- Hur kapslad komprehension läses (`for x in ... for y in ...`)
- Att diktkomp och mängdkomp följer samma grammatik som listkomp

## Komma igång

```bash
uv run pytest koans/11-komprehensioner/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "print(type([x for x in range(3)]), type(x for x in range(3)))"`
- Kapslad komp: `[x*y for x in [1,2] for y in [3,4]]` — yttre loop är ytterst

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför returnerar `type(x for x in range(3))` en generator, inte en lista?
- I `[x*y for x in [1,2] for y in [10,20]]` — hur många element ger det, och i vilken ordning?
- Vad är minnesfördelen med `sum(x**2 for x in range(1_000_000))` jämfört med listkomprehension?
