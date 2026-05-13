from sentinel import ____


# === Sanningsvärdet av objekt ===


def test_empty_list_is_falsy():
    """Tomma samlingar är falsy i Python. Är [] sant eller falskt?"""
    assert bool([]) == ____


def test_nonempty_list_is_truthy_even_with_falsy_element():
    """En lista med ett element är truthy — oavsett vad elementet är.
    Är [0] sant eller falskt?"""
    assert bool([0]) == ____


def test_zero_float_is_falsy():
    """Noll är falsy oavsett taltyp. Är 0.0 sant eller falskt?"""
    assert bool(0.0) == ____


def test_none_is_falsy():
    """None representerar frånvaron av ett värde och är alltid falsy.
    Är None sant eller falskt?"""
    assert bool(None) == ____


# === and och or returnerar operander, inte booleans ===


def test_or_returns_first_truthy_operand():
    """or returnerar den första truthy operanden — inte bokstavligen True eller False.
    Vad returnerar "hej" or "standard"?"""
    assert ("hej" or "standard") == ____


def test_or_returns_right_operand_when_left_is_falsy():
    """Om den vänstra operanden är falsy returnerar or den högra operanden.
    Vad returnerar "" or "standard"?"""
    assert ("" or "standard") == ____


def test_and_short_circuits_on_first_falsy():
    """and returnerar den första falsy operanden — "standard" evalueras aldrig.
    Vad returnerar None and "hej"?"""
    assert (None and "hej") == ____


# === None-jämförelser ===


def test_none_is_not_equal_to_false():
    """None och False är båda falsy men de är inte lika värden.
    Vad returnerar x == False när x = None?"""
    x = None
    assert (x == False) == ____


def test_none_is_a_singleton():
    """Det finns bara ett None-objekt i Python — det är ett singleton.
    Pekar två variabler satta till None på exakt samma objekt?"""
    a = None
    b = None
    assert (a is b) == ____


def test_is_none_checks_identity_not_equality():
    """`is None` jämför identitet och kan inte åsidosättas av __eq__.
    Vad returnerar x is None när x = None?"""
    x = None
    assert (x is None) == ____
