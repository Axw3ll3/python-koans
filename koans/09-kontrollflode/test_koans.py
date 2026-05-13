from sentinel import ____


# === Ternärt uttryck och kedjade jämförelser ===


def test_ternary_expression_returns_value_when_condition_is_true():
    """x if villkor else y returnerar x om villkoret är sant.
    Vad returnerar "stor" if 5 > 3 else "liten"?"""
    assert ("stor" if 5 > 3 else "liten") == ____


def test_ternary_expression_returns_alternative_when_condition_is_false():
    """x if villkor else y returnerar y om villkoret är falskt.
    Vad returnerar "stor" if 5 > 10 else "liten"?"""
    assert ("stor" if 5 > 10 else "liten") == ____


def test_chained_comparison_evaluates_all_parts():
    """Python stöder kedjade jämförelser: 1 < 2 < 3 kontrollerar båda villkoren.
    Är 1 < 2 < 3 True?"""
    assert (1 < 2 < 3) == ____


def test_chained_comparison_can_be_false():
    """1 < 2 > 3 är två jämförelser: 1 < 2 och 2 > 3. Är båda sanna?"""
    assert (1 < 2 > 3) == ____


# === pass, match/case och modulo ===


def test_pass_is_a_no_operation_statement():
    """pass gör ingenting — det är ett syntaktiskt platshållare.
    Vad returnerar en funktion som bara innehåller pass?"""
    def do_nothing():
        pass
    assert do_nothing() == ____


def test_modulo_determines_odd_or_even():
    """x % 2 ger 0 för jämna tal och 1 för udda.
    Vad returnerar "udda" if 7 % 2 else "jämn"?"""
    x = 7
    assert ("udda" if x % 2 else "jämn") == ____


def test_match_case_binds_pattern_variables():
    """match/case (Python 3.10+) matchar mönster och binder variabler.
    Vad binder x till när (1, 2) matchas mot (x, y)?"""
    point = (1, 2)
    match point:
        case (x, y):
            result = x
    assert result == ____


def test_not_negates_a_falsy_value():
    """not inverterar sanningsvärdet. Vad returnerar not 0?"""
    assert (not 0) == ____
