# 07 — Dictionaries

> `.get()` returnerar None om nyckeln saknas — `d["nyckel"]` kastar KeyError.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Varför `d["nyckel"]` kastar KeyError men `d.get("nyckel")` returnerar None
- Att uppdatering av en befintlig nyckel inte ökar `len(d)`
- Hur dict comprehension fungerar
- Merge-operatorn `|` (Python 3.9+) och att höger sida vinner vid nyckelkollision

## Komma igång

```bash
uv run pytest koans/07-dictionaries/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "d = {'a': 1}; d['a'] = 2; print(len(d))"`
- `.items()` ger nyckel-värde-par, `.keys()` bara nycklar, `.values()` bara värden

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad är skillnaden mellan `d["x"]` och `d.get("x", 0)` när "x" inte finns?
- Vad händer med `len(d)` om du skriver `d["a"] = 1` och sedan `d["a"] = 2`? Varför?
- Vad itererar du över när du skriver `for k in d:`? Vad skriver du för att få både nyckel och värde?
