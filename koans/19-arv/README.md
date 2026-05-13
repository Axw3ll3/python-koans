# 19 — Arv

> MRO — Method Resolution Order — avgör vilken förälderklass som vinner vid multipelt arv. Python använder C3-linjärisering.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Hur Python hittar en metod (letar i `__mro__`-ordning)
- Varför `super().__init__()` behövs och vad som händer om du glömmer det
- Att `isinstance(c, A)` är True även om `c` är en instans av ett barnbarnbarn till A
- Hur diamond-problemet löses i Python via MRO

## Komma igång

```bash
uv run pytest koans/19-arv/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "class A: pass; class B(A): pass; print(B.__mro__)"`
- `issubclass(B, A)` är True om B ärver från A — direkt eller indirekt

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer om `__init__` i en subklass inte anropar `super().__init__()`?
- Vad är MRO och varför behövs det? Ge ett exempel med multipelt arv.
- Vad returnerar `isinstance(C(), A)` om `class C(B)` och `class B(A)`? Varför?
