# 05 — Listor

> Listor är mutabla sekvenser — och mutabilitet har fallgropar som inte finns i C#-arrayer eller Java-listor.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Skillnaden mellan `append` (ett element) och `extend` (en iterable)
- Varför `[[]] * 3` skapar tre listor som delar identitet
- Att `sort()` muterar originalet, men `sorted()` returnerar en ny lista
- Att slicning (`a[:]`) kopierar listan ytligt, inte djupt

## Komma igång

```bash
uv run pytest koans/05-listor/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "a = [[]] * 3; a[0].append(1); print(a)"`
- `append()` returnerar None, inte listan

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför ser alla tre listorna likadana ut efter `a = [[]] * 3; a[0].append(1)`? Vad skapar `*`-operatorn?
- Vad är skillnaden mellan `lst.sort()` och `sorted(lst)`? När använder du vilket?
- Vad händer med `lst` efter `lst2 = lst + [4]`? Och efter `lst.extend([4])`? Varför skiljer de sig?
