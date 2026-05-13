from sentinel import ____


# === Returvärde och standardargument ===


def test_function_without_return_yields_none():
    """En funktion utan return-sats returnerar implicit None.
    Vad returnerar en funktion som bara innehåller pass?"""
    def f():
        pass
    assert f() == ____


def test_default_argument_is_used_when_not_provided():
    """Standardargument används om anroparen inte skickar ett värde.
    Vad returnerar greet() när name har standardvärdet "världen"?"""
    def greet(name="världen"):
        return f"Hej {name}!"
    assert greet() == ____


def test_mutable_default_argument_persists_between_calls():
    """Standardargument evalueras en gång vid funktionsdefinition — inte per anrop.
    Vad är längden på den returnerade listan vid tredje anropet av f()?"""
    def f(lst=[]):
        lst.append(1)
        return lst
    f()
    f()
    assert len(f()) == ____


def test_none_default_is_the_idiomatic_fix_for_mutable_defaults():
    """Lösningen: använd None som standard och skapa listan inuti funktionen.
    Är lst en ny tom lista om inget argument skickas?"""
    def f(lst=None):
        if lst is None:
            lst = []
        lst.append(1)
        return lst
    assert f() == ____


# === *args och **kwargs ===


def test_star_args_collects_positional_arguments_as_tuple():
    """*args samlar alla icke-namngivna argument i en tupel.
    Vilken typ är args i def f(*args)?"""
    def f(*args):
        return type(args)
    assert f(1, 2, 3) == ____


def test_kwargs_collects_keyword_arguments_as_dict():
    """**kwargs samlar alla namngivna argument i ett dict.
    Vilken typ är kwargs i def f(**kwargs)?"""
    def f(**kwargs):
        return type(kwargs)
    assert f(a=1, b=2) == ____


# === Keyword-only och funktioner som objekt ===


def test_keyword_only_parameter_must_be_passed_by_name():
    """Parametrar efter * i signaturen måste skickas som nyckelordsargument.
    Kastar f(1, 2) TypeError när signaturen är def f(a, *, b)?"""
    import pytest
    def f(a, *, b):
        return a + b
    with pytest.raises(____):
        f(1, 2)


def test_functions_are_objects_of_type_function():
    """Funktioner är objekt och har en typ som alla andra värden.
    Vad är typen av en funktion definierad med def?"""
    def f():
        pass
    import types
    assert type(f) == ____
