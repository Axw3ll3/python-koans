# 12 — Funktioner

> Mutable standardargument evalueras en gång vid funktionsdefinition — inte vid varje anrop. Det är en av Pythons vanligaste fallgropar.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vad en funktion utan `return` returnerar
- Varför `def f(lst=[]):` är farligt och vad man gör i stället
- Skillnaden mellan `*args` (tupel av positionella argument) och `**kwargs` (dict av nyckelordsargument)
- Vad keyword-only (`*`) och positional-only (`/`) parametrar är

## Komma igång

```bash
uv run pytest koans/12-funktioner/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "def f(lst=[]): lst.append(1); return lst; print(f(), f(), f())"`
- Funktioner är objekt — `type(f)` returnerar `<class 'function'>`

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer om du anropar `f()` tre gånger när `f` är `def f(lst=[]): lst.append(1); return lst`? Varför?
- Vad är lösningen på mutable-default-problemet? Varför fungerar `def f(lst=None): lst = lst or []`?
- Vad är skillnaden mellan en parameter definierad efter `*` (keyword-only) och en vanlig parameter?
