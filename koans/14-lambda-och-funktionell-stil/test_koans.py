from sentinel import ____


# === Lambda ===


def test_lambda_is_an_anonymous_function():
    """lambda x: x * 2 skapar ett namnlöst funktionsobjekt som kan anropas direkt.
    Vad returnerar (lambda x: x * 2)(5)?"""
    assert (lambda x: x * 2)(5) == ____


def test_sorted_with_key_sorts_by_derived_value():
    """sorted(key=func) sorterar baserat på nyckelns returvärde — inte elementets ursprungsvärde.
    Vilket element hamnar först om listan sorteras efter stränglängd?"""
    words = ["banan", "äpple", "kiwi"]
    assert sorted(words, key=len)[0] == ____


# === map och filter ===


def test_map_applies_function_to_each_element():
    """map(func, iterable) applicerar func på varje element.
    Vad returnerar list(map(lambda x: x**2, [1, 2, 3]))?"""
    assert list(map(lambda x: x**2, [1, 2, 3])) == ____


def test_filter_keeps_elements_where_function_returns_true():
    """filter(func, iterable) behåller element där func returnerar True.
    Vad returnerar list(filter(lambda x: x > 2, [1, 2, 3, 4]))?"""
    assert list(filter(lambda x: x > 2, [1, 2, 3, 4])) == ____


def test_map_returns_a_lazy_iterator():
    """map() returnerar en lat iterator — inget beräknas förrän du itererar.
    Vad är typen av map(str, [1, 2])?"""
    assert type(map(str, [1, 2])) == ____


# === functools ===


def test_reduce_accumulates_a_result():
    """reduce(func, iterable) applicerar func kumulativt från vänster.
    Vad returnerar reduce(lambda a, b: a + b, [1, 2, 3, 4])?"""
    from functools import reduce
    assert reduce(lambda a, b: a + b, [1, 2, 3, 4]) == ____


def test_partial_creates_a_function_with_preset_arguments():
    """partial(func, **preset) skapar en ny funktion med förinställda argument.
    Vad returnerar double(5) om double = partial(lambda x, n: x*n, n=2)?"""
    from functools import partial
    double = partial(lambda x, n: x * n, n=2)
    assert double(5) == ____


def test_lambda_cannot_contain_statements():
    """Lambda kan bara innehålla ett uttryck — inte satser som tilldelning.
    Kastar lambda x: x = 1 ett SyntaxError?"""
    import pytest
    with pytest.raises(____):
        eval("lambda x: x = 1")
