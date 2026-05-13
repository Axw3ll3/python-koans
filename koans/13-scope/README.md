# 13 — Scope

> Python letar upp ett namn i LEGB-ordning: Local → Enclosing → Global → Builtin. Tilldelning utan `global` skapar alltid en lokal variabel.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Varför `x += 1` i en funktion kastar UnboundLocalError om `x` är en global variabel
- Vad `global` och `nonlocal` gör
- Hur en closure fångar variabler från omgivande scope
- Loop-closure-fallgropen: `lambda: i` i en loop fångar `i` vid körtid, inte vid definition

## Komma igång

```bash
uv run pytest koans/13-scope/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- LEGB: Python *läser* ett namn globalt, men kräver `global` för att *skriva* till det
- Loop-closure: alla lambdas delar samma `i`-variabel — de fångar referensen, inte värdet

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför kastar `def f(): x += 1` ett UnboundLocalError när `x` är definierad globalt?
- Vad returnerar `funcs[0]()` om `funcs = [lambda: i for i in range(3)]`? Varför — och hur fixar man det?
- Vad är en closure? Ge ett exempelscenario där den är användbar.
