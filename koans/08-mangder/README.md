# 08 — Mängder

> Mängder lagrar unika element utan garanterad ordning — och ger O(1)-uppslagning oavsett storlek.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Varför `{1, 2, 2, 3}` har tre element, inte fyra
- Skillnaden mellan union (`|`), snitt (`&`), differens (`-`) och symmetrisk differens (`^`)
- Varför `{1, 2, 3}[0]` kastar TypeError
- Vad frozenset är och när det behövs

## Komma igång

```bash
uv run pytest koans/08-mangder/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "s = {1, 2, 2, 3}; print(s, len(s))"`
- `{}` är ett tomt dict, inte ett tomt set — använd `set()` för ett tomt mängd

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför kastar `{1, 2, 3}[0]` ett undantag? Vad är det grundläggande antagandet som saknas i ett set?
- Vad är skillnaden mellan `s1 - s2` och `s2 - s1`? Är mängddifferens kommutativ?
- Varför kan en lista inte vara ett element i ett set, men en tupel kan?
