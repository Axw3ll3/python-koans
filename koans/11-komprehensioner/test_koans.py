from sentinel import ____


# === Listkomprehension ===


def test_list_comprehension_squares_each_element():
    """[uttryck for variabel in iterable] bygger en lista med transformerade element.
    Vad returnerar [x**2 for x in range(4)]?"""
    assert [x**2 for x in range(4)] == ____


def test_list_comprehension_with_filter():
    """if-klausulen filtrerar elementen — bara de som uppfyller villkoret tas med.
    Vad returnerar [x for x in range(10) if x % 2 == 0]?"""
    assert [x for x in range(10) if x % 2 == 0] == ____


def test_list_comprehension_produces_a_list():
    """[...]-syntaxen skapar alltid en lista.
    Vilken typ är [x for x in range(3)]?"""
    assert type([x for x in range(3)]) == ____


# === Generator-uttryck ===


def test_generator_expression_is_not_a_list():
    """(...)-syntaxen utan listparentes skapar ett generatoruttryck — inte en lista.
    Vilken typ är (x for x in range(3))?"""
    assert type(x for x in range(3)) == ____


def test_generator_expression_works_with_sum():
    """Generatoruttryck kan skickas direkt till sum() — inget mellanliggande list-objekt skapas.
    Vad är summan av kvadraterna för 0, 1, 2, 3?"""
    assert sum(x**2 for x in range(4)) == ____


# === Dict- och mängdkomprehension ===


def test_dict_comprehension_creates_a_dict():
    """Dict comprehension använder {nyckel: värde for ...}-syntaxen.
    Vad returnerar {x: x**2 for x in range(3)}?"""
    assert {x: x**2 for x in range(3)} == ____


def test_set_comprehension_creates_a_set_of_unique_values():
    """{uttryck for ...} skapar en mängd — dubbletter elimineras.
    Hur många unika rester finns i {x % 3 for x in range(6)}?"""
    assert len({x % 3 for x in range(6)}) == ____


# === Kapslad komprehension ===


def test_nested_comprehension_produces_cross_product():
    """Kapslad komprehension med två for-satser ger kartesisk produkt.
    Hur många element ger [x*y for x in [1,2] for y in [10,20]]?"""
    assert len([x * y for x in [1, 2] for y in [10, 20]]) == ____
