# Python Koaner

Learn Python's idioms and mental models by solving deliberately failing tests.

**Who this is for:** Programmers who know another language (C#, JavaScript, Java) but not Python specifically.

---

## Setup

### 1. Fork this repository

Click **Fork** on GitHub. Work in your own fork — do not push directly to the original.

### 2. Clone your fork

```bash
git clone git@github.com:<your-username>/python-koans.git
cd python-koans
```

### 3. Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 4. Install dependencies

```bash
uv sync
```

---

## Working through a module

1. Read the module README — understand what you are training and what is expected
2. Open `test_koans.py`
3. Run: `uv run pytest koans/NN-modulename/ -x --tb=short`
4. Read the first failing test — the docstring tells you what to figure out
5. Replace `____` with what you think is the correct answer
6. Run pytest again
7. Repeat until all tests are green
8. Confirm with `-v`: `uv run pytest koans/NN-modulename/ -v`
9. Work through the "Can you explain it?" questions in the module README — without looking at the koans
10. **Commit** (see below)
11. Move to the next module

### Recommended: file watching

```bash
uv run pytest-watch -- koans/NN-modulename/ -x --tb=short
```

Save the file → tests re-run automatically.

---

## Committing your work

**Commit once per completed module.** Each commit message is your reflection on that module — it is read by your teacher and forms part of the assessment.

A commit message must be a single sentence. It should capture one of:

- something you learned
- an insight or surprise
- what was difficult and why
- a mental model that shifted

```bash
git add koans/01-grunderna/test_koans.py
git commit -m "Surprised that a = b creates a reference rather than a copy, unlike C# value types."
```

```bash
git commit -m "The banker's rounding in round() was unexpected — always assumed Python rounded 0.5 up."
```

```bash
git commit -m "LEGB scoping clicked when I understood that assignment inside a function always creates a local."
```

**One sentence. Your own words. No filler.**

Bad examples:
- `"Solved module 03"` — says nothing about understanding
- `"Fixed the tests"` — not a reflection
- `"All green"` — empty

---

## What is expected

Green tests are necessary but not sufficient.

You should be able to:
1. **Explain** why the correct answer is correct — not just that it is
2. **Predict** what happens if you change something in a koan
3. **Answer** the "Can you explain it?" questions in each module README without looking at the koans

In a course context you may be asked to demonstrate your understanding verbally.

---

## Module overview

| # | Module | Level |
|---|---|---|
| 01 | Grunderna | Foundation |
| 02 | Tal | Foundation |
| 03 | Strängar | Foundation |
| 04 | Booleaner och None | Foundation |
| 05 | Listor | Foundation |
| 06 | Tupler | Foundation |
| 07 | Dictionaries | Foundation |
| 08 | Mängder | Foundation |
| 09 | Kontrollflöde | Core |
| 10 | Loopar | Core |
| 11 | Komprehensioner | Core |
| 12 | Funktioner | Core |
| 13 | Scope | Core |
| 14 | Lambda och funktionell stil | Core |
| 15 | Generatorer | Core |
| 16 | Undantag | Core |
| 17 | Kontexthanterare | Core |
| 18 | Klasser | Advanced |
| 19 | Arv | Advanced |
| 20 | Dunder-metoder | Advanced |
| 21 | Moduler och paket | Advanced |
| 22 | Standardbiblioteket | Advanced |
| 23 | Typledtrådar | Advanced |
| 24 | Dekoratorer | Advanced |
| 25 | Dataklasser | Advanced |
| 26 | Repetition | Repetition |

Experienced programmers from another language can start at module 09.

---

## Tools

```bash
uv run pytest                               # run all tests
uv run pytest koans/01-grunderna/ -v       # run one module with details
uv run ruff check koans/                   # lint
uv run ruff format koans/                  # format
uv run pyright koans/                      # type checking
```
