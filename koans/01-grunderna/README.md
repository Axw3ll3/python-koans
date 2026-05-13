# 01 — Grunderna

> I Python binder du namn till objekt — inte till minnesplatser som i C# eller Java.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att `a = b` skapar en referens till samma objekt, inte en kopia
- Skillnaden mellan `is` (identitet) och `==` (värde)
- Vad `type()` returnerar och varför Python kallas dynamiskt typat
- Vad `id()` är och när `is` kan ge överraskande resultat

## Komma igång

```bash
uv run pytest koans/01-grunderna/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga — den ger kontext och ställer exakt rätt fråga
- Testa i Python-tolken: `python -c "a = []; b = a; b.append(1); print(a)"`
- Sök på frågan i docstringen, inte på felmeddelandet

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer med `len(a)` om du skriver `a = [1, 2, 3]; b = a; b.append(4)`? Varför?
- Varför returnerar `a is b` ibland True för `a = 42; b = 42` men inte alltid för listor med samma värde?
- Vad är skillnaden mellan `type(x) == int` och `isinstance(x, int)`? Varför föredrar Python `isinstance`?
