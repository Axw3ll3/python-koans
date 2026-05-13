# 14 — Lambda och funktionell stil

> `map` och `filter` returnerar lata iterables — de beräknar inget förrän du itererar över dem.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att `lambda x: x * 2` är ett uttryck, inte ett statement — ingen `return`, ingen tilldelning
- Att `map()` och `filter()` är lata — de evalueras inte vid skapande
- Hur `sorted(key=...)` fungerar och varför det är kraftfullare än att sortera på värden direkt
- Vad `functools.partial` gör

## Komma igång

```bash
uv run pytest koans/14-lambda-och-funktionell-stil/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "from functools import reduce; print(reduce(lambda a, b: a + b, [1,2,3,4]))"`
- `type(map(str, [1,2]))` returnerar en map-iterator, inte en lista

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför kan du inte skriva `lambda x: x = 1`? Vad är den fundamentala begränsningen i ett lambda?
- Vad returnerar `type(map(str, [1, 2, 3]))`? Varför är det en iterator och inte en lista?
- Hur sorterar `sorted(ord, key=len)` en lista av strängar efter längd? Vad gör `key`-argumentet exakt?
