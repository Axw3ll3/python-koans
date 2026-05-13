from sentinel import ____


# === with-satsen och filhantering ===


def test_with_block_closes_file_on_exit():
    """with-satsen garanterar att __exit__ anropas när blocket avslutas.
    Är filen stängd direkt efter with-blocket?"""
    import tempfile, os
    path = tempfile.mktemp()
    open(path, "w").close()
    with open(path) as f:
        pass
    assert f.closed == ____
    os.unlink(path)


def test_exit_is_called_even_when_exception_is_raised():
    """__exit__ anropas även om ett undantag kastas inuti with-blocket.
    Är filen stängd även när ett undantag kastades?"""
    import tempfile, os, pytest
    path = tempfile.mktemp()
    open(path, "w").close()
    f = None
    with pytest.raises(ValueError):
        with open(path) as f:
            raise ValueError("test")
    assert f.closed == ____
    os.unlink(path)


# === contextlib.contextmanager ===


def test_contextmanager_yield_separates_setup_from_teardown():
    """Koden före yield är setup, koden efter yield är teardown.
    Vad returnerar kontexthanteraren som det hanterade värdet (as-variabeln)?"""
    from contextlib import contextmanager

    @contextmanager
    def managed():
        value = "hej"
        yield value

    with managed() as v:
        assert v == ____


def test_contextmanager_teardown_runs_after_block():
    """Koden efter yield körs när with-blocket avslutas.
    Vad innehåller log efter with-blocket?"""
    from contextlib import contextmanager

    log = []

    @contextmanager
    def tracked():
        log.append("in")
        yield
        log.append("out")

    with tracked():
        pass

    assert log == ____


# === Kapslade kontexthanterare och exit-ordning ===


def test_exit_is_called_in_reverse_order_for_nested_managers():
    """Vid kapslade kontexthanterare anropas __exit__ i omvänd ordning (LIFO).
    Vilket värde lämnar with A() as a, B() as b: sist i log?"""
    from contextlib import contextmanager

    log = []

    @contextmanager
    def cm(name):
        log.append(f"enter {name}")
        yield
        log.append(f"exit {name}")

    with cm("A"), cm("B"):
        pass

    assert log[-1] == ____


def test_suppressing_exception_by_returning_true_from_exit():
    """En kontexthanterare som returnerar True från __exit__ undertrycker undantaget.
    Kastas undantaget vidare om __exit__ returnerar True?"""
    from contextlib import suppress

    exception_escaped = False
    try:
        with suppress(ValueError):
            raise ValueError("undertryckt")
    except ValueError:
        exception_escaped = True

    assert exception_escaped == ____
