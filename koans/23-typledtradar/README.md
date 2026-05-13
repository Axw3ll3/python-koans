# 23 — Typledtrådar

> Typledtrådar är metadata — de påverkar inte runtime-beteendet. En funktion annoterad med `x: int` accepterar vilken typ som helst vid körning.

## Det här tränar du

Efter den här modulen ska du kunna förklara:

- Att typledtrådar inte enforças av Python vid runtime
- Att `int | None` och `Optional[int]` är ekvivalenta, och vilken som är modern (3.10+)
- Att `list[int]` (3.9+) är att föredra framför `List[int]` från `typing`
- Vad `Protocol` är och hur det möjliggör strukturell subtypning

## Komma igång

```bash
uv run pytest koans/23-typledtradar/ -x --tb=short
```

## Om du fastnar

- Läs docstringen noga
- Testa: `python -c "def f(x: int) -> str: return str(x); print(f('hej'))"`
- `reveal_type()` är ett pyright/mypy-direktiv — inte en inbyggd Python-funktion

## Kan du förklara det?

Testa dig själv utan att titta på koanerna:

- Vad händer vid runtime om du anropar `f("hej")` när `f` är `def f(x: int) -> str:`? Kastas ett undantag?
- Vad är skillnaden mellan nominell subtypning (arv) och strukturell subtypning (`Protocol`)?
- Varför är `list[int]` att föredra framför `List[int]` från `typing` i Python 3.9+?
