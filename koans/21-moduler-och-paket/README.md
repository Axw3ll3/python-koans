# 21 — Moduler och paket

> `__name__` är `"__main__"` om filen körs direkt — annars är det modulens namn. Det är kärnan i `if __name__ == "__main__":`.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Skillnaden mellan `__name__` i ett direkt kört skript och i en importerad modul
- Varför `__init__.py` gör en katalog till ett paket
- Vad som händer vid en cirkulär import
- Vad `sys.path` är och varför det spelar roll

## Komma igång

```bash
uv run pytest koans/21-moduler-och-paket/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: skapa `mod.py` med `print(__name__)`, kör direkt med `python mod.py`, sedan `python -c "import mod"`
- `from math import sqrt` importerar `sqrt` till nuvarande namnrymd — `math.sqrt` behövs inte

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad är `__name__` när en fil importeras? Och när den körs direkt?
- Vad är skillnaden mellan `import math` och `from math import sqrt`? När föredrar du vilket?
- Varför kan en cirkulär import orsaka problem? Vad händer steg för steg?
