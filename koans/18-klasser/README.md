# 18 — Klasser

> Klassattribut delas av alla instanser — mutation via en instans syns för alla. Instansattribut som sätts i `__init__` är säkra.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Skillnaden mellan instansattribut (sätts i `__init__`) och klassattribut (sätts på klassen)
- Varför ett mutable klassattribut är en fallgrop
- Vad `@property`, `@staticmethod` och `@classmethod` gör
- Skillnaden mellan `__str__` och `__repr__` och när respektive anropas

## Komma igång

```bash
uv run pytest koans/18-klasser/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "class A: x = []; a = A(); b = A(); a.x.append(1); print(b.x)"`
- `@classmethod` tar `cls` (klassen) som första argument, `@staticmethod` tar ingen automatisk parameter

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer med `b.options` om `a.options.append("debug")` när `options` är ett klassattribut? Varför?
- Vad returnerar `__init__` implicit? Vad händer om du skriver `return self` i `__init__`?
- Vad är skillnaden mellan `__str__` och `__repr__`? Vilken anropas av `print()`?
