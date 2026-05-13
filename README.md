# Python Koaner

Lär dig Pythons idiom och mentala modeller genom att lösa failande tester.

**Målgrupp:** Du som kan ett annat programmeringsspråk (C#, JavaScript, Java) men inte Python specifikt.

---

## Installation

### 1. Installera uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Klona och synkronisera

```bash
git clone https://github.com/<org>/python-koaner
cd python-koaner
uv sync
```

---

## Komma igång

Börja med modul 01. Läs modulens README innan du öppnar testfilen.

```bash
# Läs vad modulen tränar
cat koans/01-grunderna/README.md

# Starta modulen
uv run pytest koans/01-grunderna/ -x --tb=short
```

---

## Arbetsflöde per modul

1. Läs modulens `README.md` — förstå vad du tränar och vad som förväntas
2. Öppna `test_koans.py`
3. Kör: `uv run pytest koans/NN-modulnamn/ -x --tb=short`
4. Läs det första failande testet — docstringen förklarar vad du ska ta reda på
5. Ersätt `____` med vad du tror är rätt svar
6. Kör pytest igen
7. Upprepa tills alla tester är gröna
8. Bekräfta med `-v`: `uv run pytest koans/NN-modulnamn/ -v`
9. Gå igenom "Kan du förklara det?"-frågorna i README:n — utan att titta på koanerna
10. Gå till nästa modul

### Rekommenderat: filövervakning

```bash
uv run pytest-watch -- koans/NN-modulnamn/ -x --tb=short
```

Sparar du filen → körs testerna om automatiskt.

---

## Vad förväntas av dig?

Gröna tester är ett nödvändigt men inte tillräckligt villkor för förståelse.

Du ska kunna:
1. **Förklara** varför rätt svar är rätt — inte bara att det är det
2. **Förutsäga** vad som händer om du ändrar något i koanens kod
3. **Svara** på "Kan du förklara det?"-frågorna i varje moduls README utan att titta på koanerna

I en kurskontext kan du behöva redovisa din förståelse muntligt.

---

## Modulöversikt

| # | Modul | Band |
|---|---|---|
| 01 | Grunderna | Grund |
| 02 | Tal | Grund |
| 03 | Strängar | Grund |
| 04 | Booleaner och None | Grund |
| 05 | Listor | Grund |
| 06 | Tupler | Grund |
| 07 | Dictionaries | Grund |
| 08 | Mängder | Grund |
| 09 | Kontrollflöde | Kärna |
| 10 | Loopar | Kärna |
| 11 | Komprehensioner | Kärna |
| 12 | Funktioner | Kärna |
| 13 | Scope | Kärna |
| 14 | Lambda och funktionell stil | Kärna |
| 15 | Generatorer | Kärna |
| 16 | Undantag | Kärna |
| 17 | Kontexthanterare | Kärna |
| 18 | Klasser | Avancerat |
| 19 | Arv | Avancerat |
| 20 | Dunder-metoder | Avancerat |
| 21 | Moduler och paket | Avancerat |
| 22 | Standardbiblioteket | Avancerat |
| 23 | Typledtrådar | Avancerat |
| 24 | Dekoratorer | Avancerat |
| 25 | Dataklasser | Avancerat |
| 26 | Repetition | Repetition |

En erfaren programmerare från ett annat språk kan börja vid modul 09.

---

## Verktyg

```bash
uv run pytest                              # kör alla tester
uv run pytest koans/01-grunderna/ -v      # kör en modul med detaljer
uv run ruff check koans/                  # lint
uv run ruff format koans/                 # format
uv run pyright koans/                     # typkontroll
```
