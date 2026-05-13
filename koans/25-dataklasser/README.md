# 25 — Dataklasser

> `field(default_factory=list)` — inte `field(default=[])`. Mutable defaults i dataklasser kastar TypeError vid klassdefinition.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Vad `@dataclass` genererar automatiskt (`__init__`, `__repr__`, `__eq__`)
- Varför `field(default=[])` kastar TypeError och hur `default_factory` löser det
- Vad `frozen=True` gör och vad det kostar
- Hur `dataclasses.replace()` och `dataclasses.asdict()` fungerar

## Komma igång

```bash
uv run pytest koans/25-dataklasser/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "from dataclasses import dataclass; @dataclass\nclass P:\n    x: int = 0\nprint(P())"`
- `__post_init__` anropas automatiskt av den genererade `__init__` — efter att attributen satts

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför kastar `field(default=[])` TypeError vid klassdefinition? Vad är problemet?
- Vad gör `dataclasses.replace(p, x=5)`? Muterar det `p` eller returnerar det ett nytt objekt?
- Vad är skillnaden mellan `@dataclass` och `@dataclass(frozen=True)`? Vad är priset för `frozen=True`?
