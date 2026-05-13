# 22 — Standardbiblioteket

> `pathlib.Path` låter dig hantera filsystemssökvägar med `/`-operatorn i stället för strängkonkatenering.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Hur `pathlib.Path` och `/`-operatorn fungerar för att bygga sökvägar
- Vad `collections.Counter`, `defaultdict` och `namedtuple` löser
- Hur `datetime.date` och `timedelta` hanterar datum och differenser
- Vad `json.dumps` och `json.loads` kräver av nycklar och värden

## Komma igång

```bash
uv run pytest koans/22-standardbiblioteket/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "from pathlib import Path; p = Path('a') / 'b' / 'c.txt'; print(p, p.suffix)"`
- `defaultdict(list)["ej_nyckel"]` returnerar en tom lista — det kastar ingen exception

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad returnerar `Path("a/b/c.txt").suffix`? Och `.stem`? Och `.parent`?
- Vad händer om du läser en nyckel som inte finns i en `defaultdict(list)`? Varför är det annorlunda mot en vanlig dict?
- Varför misslyckas `json.dumps({1: "a"})`? Vad kräver JSON av nycklar?
