from sentinel import ____


# === Inbyggda operatorer och dunder-metoder ===


def test_len_calls_dunder_len():
    """len(obj) anropar obj.__len__(). En klass kan implementera __len__ för att stödja len().
    Vad returnerar len(r) om r.__len__ returnerar 42?"""
    class R:
        def __len__(self):
            return 42
    assert len(R()) == ____


def test_getitem_enables_index_access():
    """r[5] anropar r.__getitem__(5). En klass kan implementera __getitem__ för indexering.
    Vad returnerar r[5] om __getitem__ returnerar i * 2?"""
    class R:
        def __getitem__(self, i):
            return i * 2
    r = R()
    assert r[5] == ____


def test_add_calls_dunder_add():
    """a + b anropar a.__add__(b). Vilken dunder-metod implementerar du för att stödja +?"""
    class Vec:
        def __init__(self, x):
            self.x = x
        def __add__(self, other):
            return Vec(self.x + other.x)
    v = Vec(1) + Vec(2)
    assert v.x == ____


def test_contains_is_called_by_in_operator():
    """5 in obj anropar obj.__contains__(5).
    Är 5 in r True om __contains__ returnerar True för alla värden?"""
    class R:
        def __contains__(self, item):
            return True
    assert (5 in R()) == ____


# === __eq__, __hash__ och __bool__ ===


def test_implementing_eq_sets_hash_to_none():
    """När du implementerar __eq__ sätter Python automatiskt __hash__ = None.
    Vad är hash(obj) när __eq__ är implementerad men inte __hash__?"""
    import pytest
    class Punkt:
        def __init__(self, x, y):
            self.x, self.y = x, y
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
    p = Punkt(1, 2)
    with pytest.raises(____):
        hash(p)


def test_bool_calls_dunder_bool():
    """bool(obj) anropar obj.__bool__(). En klass med __bool__ som returnerar False är falsy.
    Vad returnerar bool(c) om __bool__ returnerar False?"""
    class C:
        def __bool__(self):
            return False
    assert bool(C()) == ____


# === Iterator-protokollet och __call__ ===


def test_iter_and_next_implement_iterator_protocol():
    """En klass med __iter__ och __next__ kan användas i for-loopar.
    Vad är typen av iter(obj) om obj implementerar __iter__ (returnerar self) och __next__?"""
    class Räknare:
        def __init__(self, max):
            self.max = max
            self.n = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.n >= self.max:
                raise StopIteration
            self.n += 1
            return self.n
    assert list(Räknare(3)) == ____


def test_call_makes_instance_callable():
    """__call__ gör en instans anropbar — obj() anropar obj.__call__().
    Vad returnerar mul(4) om __call__ returnerar self.faktor * x och faktor = 3?"""
    class Multiplikator:
        def __init__(self, faktor):
            self.faktor = faktor
        def __call__(self, x):
            return self.faktor * x
    mul = Multiplikator(3)
    assert mul(4) == ____
