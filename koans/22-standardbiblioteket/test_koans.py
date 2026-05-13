from sentinel import ____


# === pathlib ===


def test_path_slash_operator_creates_a_path_instance():
    """Path / "del" bygger sökvägar med operatorn / istället för strängkonkatenering.
    Är resultatet av Path("a") / "b" / "c.txt" en instans av Path?"""
    from pathlib import Path
    assert isinstance(Path("a") / "b" / "c.txt", Path) == ____


def test_path_suffix_returns_file_extension():
    """Path.suffix returnerar filändelsen inklusive punkten.
    Vad returnerar Path("a/b/c.txt").suffix?"""
    from pathlib import Path
    assert Path("a/b/c.txt").suffix == ____


# === collections ===


def test_counter_counts_element_occurrences():
    """Counter räknar förekomster av varje element i en iterable.
    Hur många 's' finns i "mississippi"?"""
    from collections import Counter
    assert Counter("mississippi")["s"] == ____


def test_defaultdict_returns_default_for_missing_key():
    """defaultdict(list) returnerar en ny tom lista för saknade nycklar — kastar ingen KeyError.
    Vad returnerar defaultdict(list)["ej_nyckel"]?"""
    from collections import defaultdict
    assert defaultdict(list)["ej_nyckel"] == ____


def test_namedtuple_allows_attribute_access():
    """namedtuple skapar en tuppelklass med namngivna fält.
    Vad returnerar p.x om p = P(1, 2) och P = namedtuple("P", ["x", "y"])?"""
    from collections import namedtuple
    P = namedtuple("P", ["x", "y"])
    p = P(1, 2)
    assert p.x == ____


# === datetime ===


def test_date_subtraction_returns_timedelta():
    """Subtraktion av två date-objekt returnerar ett timedelta-objekt.
    Vilken typ är date(2026, 5, 1) - date(2026, 4, 1)?"""
    from datetime import date
    assert type(date(2026, 5, 1) - date(2026, 4, 1)) == ____


def test_timedelta_days_attribute_gives_number_of_days():
    """timedelta.days ger antalet hela dygn i tidsskillnaden.
    Hur många dagar är skillnaden mellan 1 maj och 1 april 2026?"""
    from datetime import date, timedelta
    diff = date(2026, 5, 1) - date(2026, 4, 1)
    assert diff.days == ____


# === json ===


def test_json_dumps_converts_dict_to_string():
    """json.dumps() serialiserar ett Python-objekt till en JSON-sträng.
    Vilken typ returnerar json.dumps({"a": 1})?"""
    import json
    assert type(json.dumps({"a": 1})) == ____


def test_json_converts_integer_keys_to_strings():
    """json.dumps() konverterar heltalsnycklar till strängar — det höjer inget undantag.
    Vad är nyckeln i det återladdade dictet om originalet hade int-nyckel 1?"""
    import json
    result = json.loads(json.dumps({1: "hej"}))
    assert list(result.keys())[0] == ____
