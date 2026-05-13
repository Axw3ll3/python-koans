from sentinel import ____


# === @dataclass genererar metoder ===


def test_dataclass_generates_init_and_repr():
    """@dataclass genererar __init__ och __repr__ automatiskt.
    Innehåller repr(p) klassnamnet och fältvärdena?"""
    from dataclasses import dataclass

    @dataclass
    class Punkt:
        x: int
        y: int

    p = Punkt(1, 2)
    assert ("Punkt" in repr(p)) == ____


def test_dataclass_generates_eq_based_on_fields():
    """@dataclass genererar __eq__ som jämför fältvärdena.
    Är Punkt(1, 2) == Punkt(1, 2)?"""
    from dataclasses import dataclass

    @dataclass
    class Punkt:
        x: int
        y: int

    assert (Punkt(1, 2) == Punkt(1, 2)) == ____


# === Mutable defaults och field() ===


def test_mutable_default_in_dataclass_raises_typeerror():
    """Mutable defaultvärden i @dataclass kastar TypeError vid klassdefinition.
    Vilken exception kastar @dataclass med fält x: list = []?"""
    import pytest
    from dataclasses import dataclass, field

    with pytest.raises(____):
        @dataclass
        class Problematisk:
            x: list = []


def test_field_default_factory_creates_new_instance_per_object():
    """field(default_factory=list) skapar en ny tom lista för varje instans.
    Delar a och b samma lista?"""
    from dataclasses import dataclass, field

    @dataclass
    class Config:
        tags: list = field(default_factory=list)

    a = Config()
    b = Config()
    a.tags.append("debug")
    assert b.tags == ____


# === frozen, replace och asdict ===


def test_frozen_dataclass_raises_on_attribute_assignment():
    """@dataclass(frozen=True) förhindrar attributsättning efter skapandet.
    Vilken exception kastar p.x = 5 när p är en frozen dataclass?"""
    import pytest
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Punkt:
        x: int
        y: int

    p = Punkt(1, 2)
    with pytest.raises(____):
        p.x = 5


def test_replace_returns_a_new_instance_with_updated_fields():
    """dataclasses.replace() returnerar en ny instans med ändrade fält — muterar inte originalet.
    Vad är p.x efter replace(p, x=99)?"""
    from dataclasses import dataclass, replace

    @dataclass
    class Punkt:
        x: int
        y: int

    p = Punkt(1, 2)
    p2 = replace(p, x=99)
    assert p.x == ____


def test_asdict_converts_dataclass_to_dict():
    """dataclasses.asdict() konverterar en dataclass till ett dict med fältnamn som nycklar.
    Vilken typ returnerar asdict(p)?"""
    from dataclasses import dataclass, asdict

    @dataclass
    class Punkt:
        x: int
        y: int

    p = Punkt(1, 2)
    assert type(asdict(p)) == ____


def test_post_init_is_called_after_field_assignment():
    """__post_init__ anropas automatiskt av den genererade __init__ efter att fälten satts.
    Vad är p.beskrivning om __post_init__ sätter den till f"({p.x}, {p.y})"?"""
    from dataclasses import dataclass

    @dataclass
    class Punkt:
        x: int
        y: int

        def __post_init__(self):
            self.beskrivning = f"({self.x}, {self.y})"

    p = Punkt(3, 4)
    assert p.beskrivning == ____
