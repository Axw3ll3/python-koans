# 02 — Tal

> Python har tre numeriska typer med distinkta beteenden — och ett par överraskningar med avrundning och floating-point.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Skillnaden mellan `/` (float-division) och `//` (heltalsdivision)
- Varför `0.1 + 0.2 == 0.3` returnerar False
- Hur `round()` fungerar i Python (bankers rounding, inte vanlig avrundning)
- Att `int` i Python har godtycklig precision — inga overflow-fel

## Komma igång

```bash
uv run pytest koans/02-tal/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "print(0.1 + 0.2)"`
- Sök på "IEEE 754 floating point" om du undrar varför 0.1 + 0.2 ≠ 0.3

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Varför returnerar `0.1 + 0.2 == 0.3` False? Vad är det egentliga värdet av `0.1 + 0.2`?
- Vad är skillnaden mellan `int(3.9)` och `round(3.9)`? Varför skiljer de sig?
- Varför avrundar `round(2.5)` nedåt till 2 i Python? Vad kallas den principen?
