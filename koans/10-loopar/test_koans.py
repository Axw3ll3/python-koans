from sentinel import ____


# === range och for-loopar ===


def test_range_produces_integers_from_zero():
    """range(n) producerar heltal från 0 upp till men inte inklusive n.
    Vad returnerar list(range(5))?"""
    assert list(range(5)) == ____


def test_range_with_start_stop_step():
    """range(start, stopp, steg) hoppar med steg.
    Vad returnerar list(range(2, 8, 2))?"""
    assert list(range(2, 8, 2)) == ____


def test_loop_variable_retains_last_value_after_loop():
    """Loopvariabeln existerar efter att loopen är klar och håller det sista värdet.
    Vad är i efter for i in range(3): pass?"""
    for i in range(3):
        pass
    assert i == ____


# === enumerate och zip ===


def test_enumerate_yields_index_value_pairs():
    """enumerate() ger (index, värde)-par vid iteration.
    Vad är det första elementet i list(enumerate(["a", "b", "c"]))?"""
    result = list(enumerate(["a", "b", "c"]))
    assert result[0] == ____


def test_enumerate_start_parameter_sets_initial_index():
    """enumerate(iterable, start=N) börjar indexera från N.
    Vad returnerar list(enumerate(["a", "b"], start=1))?"""
    assert list(enumerate(["a", "b"], start=1)) == ____


def test_zip_pairs_elements_from_two_iterables():
    """zip() parar ihop element positionellt från två iterables.
    Vad returnerar list(zip([1, 2], ["a", "b"]))?"""
    result = list(zip([1, 2], ["a", "b"]))
    assert result == ____


def test_zip_stops_at_shortest_iterable():
    """zip() stannar vid den kortaste sekvensen — extra element ignoreras.
    Hur många par ger zip([1, 2], ["a", "b", "c"])?"""
    assert len(list(zip([1, 2], ["a", "b", "c"]))) == ____


# === for/else och break ===


def test_for_else_runs_when_loop_completes_without_break():
    """else-blocket i for/else körs bara om loopen fullföljdes utan break.
    Vad sätts result till om inget break inträffar?"""
    result = "ingen break"
    for i in range(3):
        pass
    else:
        result = "fullföljd"
    assert result == ____


def test_for_else_skips_else_when_break_occurs():
    """Om break inträffar hoppas else-blocket över helt.
    Vad sätts result till om break inträffar direkt?"""
    result = "ingen break"
    for i in range(3):
        break
    else:
        result = "fullföljd"
    assert result == ____


def test_sum_of_first_ten_integers():
    """sum() med range räknar upp summer effektivt.
    Vad är summan av de tio första positiva heltalen (1–10)?"""
    assert sum(range(1, 11)) == ____
