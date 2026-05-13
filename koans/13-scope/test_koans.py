from sentinel import ____

_module_counter = 0  # används av test_global_declaration nedan


# === LEGB-regeln ===


def test_function_can_read_global_variable():
    """En funktion kan läsa en global variabel utan att deklarera den.
    Vad returnerar f() när x = 10 är global och f returnerar x?"""
    x = 10
    def f():
        return x
    assert f() == ____


def test_assignment_in_function_creates_local_variable():
    """Tilldelning inuti en funktion skapar en lokal variabel — inte global.
    Vad är den globala x efter f() när f gör x = 99?"""
    x = 10
    def f():
        x = 99
    f()
    assert x == ____


def test_augmented_assignment_to_global_raises_unboundlocalerror():
    """x += 1 inuti en funktion innebär att Python behandlar x som lokal.
    Om x inte är tilldelad lokalt kastas UnboundLocalError.
    Vilken exception kastas?"""
    import pytest
    x = 10
    def f():
        x += 1
    with pytest.raises(____):
        f()


def test_global_declaration_allows_writing_to_global():
    """global deklarerar att tilldelning ska gå till modulnivån — inte den lokala funktionen.
    Vad är _module_counter efter att f() (med global _module_counter; _module_counter += 5) körts?"""
    def f():
        global _module_counter
        _module_counter += 5
    f()
    assert _module_counter == ____


# === Closures ===


def test_closure_captures_enclosing_scope():
    """En inre funktion kan läsa variabler från omgivande scope — en closure.
    Vad returnerar outer()() när inner returnerar x och x = 1 i outer?"""
    def outer():
        x = 1
        def inner():
            return x
        return inner
    assert outer()() == ____


def test_make_adder_demonstrates_closure():
    """Closures används för att skapa specialiserade funktioner.
    Vad returnerar add5(3) om add5 = make_adder(5)?"""
    def make_adder(n):
        return lambda x: x + n
    add5 = make_adder(5)
    assert add5(3) == ____


# === Loop-closure fallgrop ===


def test_loop_closure_captures_reference_not_value():
    """Lambda i en loop fångar variabeln i — inte dess värde vid lambdans skapande.
    Vad returnerar funcs[0]() om funcs = [lambda: i for i in range(3)]?"""
    funcs = [lambda: i for i in range(3)]
    assert funcs[0]() == ____
