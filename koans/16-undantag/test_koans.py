from sentinel import ____


# === try/except och undantagstyper ===


def test_zerodivisionerror_is_raised_on_division_by_zero():
    """Division med noll kastar ett specifikt undantag.
    Vilken exception kastar 1/0?"""
    import pytest
    with pytest.raises(____):
        1 / 0


def test_valueerror_is_raised_when_conversion_fails():
    """int() kastar ett undantag om strängen inte representerar ett heltal.
    Vilken exception kastar int("abc")?"""
    import pytest
    with pytest.raises(____):
        int("abc")


def test_indexerror_is_raised_for_out_of_bounds_access():
    """Indexering utanför listans gränser kastar ett undantag.
    Vilken exception kastar [][0]?"""
    import pytest
    with pytest.raises(____):
        [][0]


# === else och finally ===


def test_else_block_runs_when_no_exception_is_raised():
    """else-blocket i try/except körs bara om inget undantag kastades i try-blocket.
    Vad sätts result till om try-blocket lyckas?"""
    result = "inget"
    try:
        x = 1 + 1
    except ValueError:
        result = "undantag"
    else:
        result = "lyckades"
    assert result == ____


def test_finally_runs_even_when_exception_is_raised():
    """finally körs alltid — oavsett om ett undantag kastades eller inte.
    Vad sätts result till om try-blocket kastar?"""
    result = "inget"
    try:
        raise ValueError("fel")
    except ValueError:
        pass
    finally:
        result = "finally"
    assert result == ____


# === raise och undantagshierarkier ===


def test_exception_message_is_accessible_via_args():
    """Undantagets meddelande är tillgängligt via args[0] eller str(e).
    Vad innehåller str(e) om raise ValueError("felmeddelande")?"""
    try:
        raise ValueError("felmeddelande")
    except ValueError as e:
        assert str(e) == ____


def test_custom_exception_inherits_from_base_class():
    """En anpassad exception som ärver från ValueError fångas av except ValueError.
    Fångas MinException av except ValueError?"""
    class MinException(ValueError):
        pass
    try:
        raise MinException("hej")
    except ValueError:
        caught = True
    assert caught == ____


def test_systemexit_inherits_from_baseexception_not_exception():
    """SystemExit och KeyboardInterrupt ärver från BaseException, inte Exception.
    Fångar except Exception ett SystemExit?"""
    caught = False
    try:
        raise SystemExit(0)
    except Exception:
        caught = True
    except SystemExit:
        caught = False
    assert caught == ____
