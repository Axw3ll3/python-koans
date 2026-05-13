from sentinel import ____


# === @-syntaxen och vad den expanderar till ===


def test_decorator_syntax_is_sugar_for_reassignment():
    """@decorator är socker för f = decorator(f). Vad returnerar decorated()?"""
    def double_result(f):
        def wrapper():
            return f() * 2
        return wrapper

    @double_result
    def get_three():
        return 3

    assert get_three() == ____


def test_decorator_without_wraps_loses_function_name():
    """Utan functools.wraps ersätts den dekorerade funktionens __name__ med wrapper-funktionens.
    Vad är get_three.__name__ om wrappern heter "wrapper"?"""
    def decorator(f):
        def wrapper():
            return f()
        return wrapper

    @decorator
    def get_three():
        return 3

    assert get_three.__name__ == ____


def test_wraps_preserves_original_function_metadata():
    """functools.wraps(f) kopierar __name__, __doc__ etc. till wrapper-funktionen.
    Vad är get_three.__name__ med functools.wraps?"""
    from functools import wraps

    def decorator(f):
        @wraps(f)
        def wrapper():
            return f()
        return wrapper

    @decorator
    def get_three():
        return 3

    assert get_three.__name__ == ____


# === Dekoratorer med argument ===


def test_decorator_factory_returns_a_decorator():
    """@repeat(3) kräver en fabriksdekoratör: repeat returnerar en dekoratör.
    Hur många gånger anropas f() om @repeat(3) appliceras?"""
    def repeat(n):
        def decorator(f):
            def wrapper():
                results = []
                for _ in range(n):
                    results.append(f())
                return results
            return wrapper
        return decorator

    @repeat(3)
    def get_one():
        return 1

    assert len(get_one()) == ____


def test_stacked_decorators_apply_bottom_up():
    """@A @B def f appliceras som A(B(f)) — B appliceras innerst (närmast f).
    Vad returnerar f() om @add_one appliceras ytterst och @double innerst?"""
    def double(f):
        return lambda: f() * 2

    def add_one(f):
        return lambda: f() + 1

    @add_one
    @double
    def get_three():
        return 3

    assert get_three() == ____


# === functools.cache ===


def test_cache_memoizes_function_results():
    """functools.cache lagrar returvärden så att samma anrop inte beräknas igen.
    Anropas den dyra beräkningen fler än en gång med @cache?"""
    from functools import cache

    call_count = []

    @cache
    def dyr(n):
        call_count.append(n)
        return n * 2

    dyr(5)
    dyr(5)
    dyr(5)
    assert len(call_count) == ____
