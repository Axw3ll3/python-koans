from sentinel import ____


# === yield och next() ===


def test_next_returns_first_yielded_value():
    """En generatorfunktion suspenderar vid yield och returnerar värdet till anroparen.
    Vad returnerar next(g) för första gången?"""
    def gen():
        yield 1
        yield 2
    g = gen()
    assert next(g) == ____


def test_generator_function_call_returns_a_generator_object():
    """Att anropa en generatorfunktion kör inte kroppen — det skapar ett generatorobjekt.
    Vilken typ är gen()?"""
    def gen():
        yield 1
    assert type(gen()) == ____


def test_list_on_generator_collects_all_values():
    """list() tömmer generatorn och samlar alla värden i en lista.
    Vad returnerar list(gen()) för gen som yieldar 1 och 2?"""
    def gen():
        yield 1
        yield 2
    assert list(gen()) == ____


# === Generatorer är ett-gångsobjekt ===


def test_exhausted_generator_yields_empty_on_second_iteration():
    """En förbrukad generator producerar inga fler värden — list() ger en tom lista.
    Vad returnerar list(g) andra gången?"""
    def gen():
        yield 1
        yield 2
    g = gen()
    list(g)
    assert list(g) == ____


def test_stopiteration_is_raised_after_last_value():
    """next() kastar StopIteration när generatorn är uttömd.
    Vilken exception kastas?"""
    import pytest
    def gen():
        yield 1
    g = gen()
    next(g)
    with pytest.raises(____):
        next(g)


# === Generator-uttryck och yield from ===


def test_generator_expression_produces_values_lazily():
    """(uttryck for ...) skapar ett generatoruttryck — beräknar ett värde i taget.
    Vad returnerar list((x**2 for x in range(3)))?"""
    assert list(x**2 for x in range(3)) == ____


def test_yield_from_delegates_to_sub_generator():
    """yield from delegerar iteration till en annan iterable — ett element i taget.
    Vad returnerar list(chain([1, 2], [3, 4]))?"""
    def chain(*iterables):
        for it in iterables:
            yield from it
    assert list(chain([1, 2], [3, 4])) == ____
