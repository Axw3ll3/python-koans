# 15 — Generatorer

> En generator är ett ett-gångsobjekt — när den är förbrukad returnerar vidare iteration ett tomt resultat, inte ett fel.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vad `yield` gör och varför funktionskroppen inte körs när funktionen anropas
- Att generatorer är ett-gångsobjekt — du kan inte iterera dem igen
- Skillnaden mellan ett generatoruttryck och en listkomprehension
- Vad `yield from` gör

## Komma igång

```bash
uv run pytest koans/15-generatorer/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "def g(): yield 1; yield 2; gen = g(); print(next(gen), next(gen))"`
- `list(gen)` efter att generatorn är förbrukad ger `[]`, inte ett fel

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer när du anropar en generatorfunktion — varför kör inte koden omedelbart?
- Vad returnerar `list(gen)` om du kör det en gång, och sedan en gång till på samma generator? Varför?
- Vad är minnesfördelen med `sum(x**2 for x in range(1_000_000))` jämfört med att bygga hela listan?
