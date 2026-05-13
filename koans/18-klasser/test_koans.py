from sentinel import ____


# === Klass, instans och __init__ ===


def test_class_produces_instances_of_its_own_type():
    """class Hund skapar en typ. type(h) ger typen av instansen.
    Vad är type(h) när h = Hund()?"""
    class Hund:
        pass
    h = Hund()
    assert type(h) == ____


def test_init_returns_none_implicitly():
    """__init__ initierar instansen men returnerar aldrig ett värde.
    Vad returnerar Hund() om __init__ avslutas utan return?"""
    class Hund:
        def __init__(self):
            self.namn = "Rex"
    assert type(Hund()) == ____


def test_missing_self_in_method_causes_typeerror_on_call():
    """En instansmetod måste ha self som första parameter.
    Vilken exception kastar h.bark() om bark saknar self?"""
    import pytest
    class Hund:
        def bark():  # noqa
            return "Voff"
    h = Hund()
    with pytest.raises(____):
        h.bark()


# === Klass- vs instansattribut ===


def test_class_attribute_is_shared_by_all_instances():
    """Klassattribut delas av alla instanser — mutation via en instans syns för alla.
    Vad innehåller b.tricks efter a.tricks.append("sitta")?"""
    class Hund:
        tricks = []
    a = Hund()
    b = Hund()
    a.tricks.append("sitta")
    assert b.tricks == ____


def test_instance_attribute_shadows_class_attribute():
    """Om en instans tilldelas ett eget attribut skuggar det klassattributet för den instansen.
    Vad är a.art efter a.art = "pudel" om Hund.art = "okänd"?"""
    class Hund:
        art = "okänd"
    a = Hund()
    a.art = "pudel"
    assert a.art == ____


# === @property, @staticmethod, @classmethod ===


def test_property_is_accessed_without_parentheses():
    """@property gör en metod anropbar som ett attribut — utan parenteser.
    Hur läser du ett @property från en instans?"""
    class Cirkel:
        def __init__(self, r):
            self.r = r
        @property
        def area(self):
            return 3.14 * self.r ** 2
    c = Cirkel(1)
    assert type(c.____) == float


def test_str_is_called_by_print_and_str():
    """__str__ anropas av str() och print(). __repr__ anropas av repr() och i REPL.
    Vad returnerar str(h) om __str__ returnerar "Hund: Rex"?"""
    class Hund:
        def __str__(self):
            return "Hund: Rex"
    h = Hund()
    assert str(h) == ____


def test_classmethod_receives_class_as_first_argument():
    """@classmethod tar cls (klassen) som första argument, inte self (instansen).
    Vad returnerar Hund.art() om art är en @classmethod som returnerar cls.__name__?"""
    class Hund:
        @classmethod
        def art(cls):
            return cls.__name__
    assert Hund.art() == ____


def test_staticmethod_has_no_implicit_first_argument():
    """@staticmethod tar varken self eller cls — det är en vanlig funktion i klassens namnrymd.
    Vad returnerar Hund.ljud() om ljud är en @staticmethod som returnerar "Voff"?"""
    class Hund:
        @staticmethod
        def ljud():
            return "Voff"
    assert Hund.ljud() == ____
