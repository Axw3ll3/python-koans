from sentinel import ____


# === Typledtrådar är metadata ===


def test_type_hints_are_not_enforced_at_runtime():
    """Typledtrådar är metadata — Python kontrollerar dem inte vid körning.
    Kastar f("hej") ett undantag om f är annoterad def f(x: int) -> str?"""
    def f(x: int) -> str:
        return str(x)
    result = f("hej")
    assert result == ____


def test_get_type_hints_returns_a_dict():
    """typing.get_type_hints() returnerar annotationerna som ett dict.
    Vilken typ returnerar get_type_hints(f)?"""
    from typing import get_type_hints
    def f(x: int) -> str:
        return str(x)
    assert type(get_type_hints(f)) == ____


# === Modern syntax för typer ===


def test_union_type_with_pipe_operator():
    """int | None är ekvivalent med Optional[int] (Python 3.10+).
    Vad är int | None == Optional[int]?"""
    from typing import Optional
    assert (int | None == Optional[int]) == ____


def test_builtin_list_is_generic_in_python_39():
    """list[int] (inbyggd generisk, 3.9+) ersätter List[int] från typing.
    Vad är typen av list[int]?"""
    assert type(list[int]) == ____


# === Protocol — strukturell subtypning ===


def test_protocol_does_not_require_explicit_inheritance():
    """Protocol definierar ett strukturellt gränssnitt — klassen behöver inte ärva det explicit.
    Uppfyller Anka protokollet Simmare om Anka har en simma()-metod?"""
    from typing import Protocol, runtime_checkable

    @runtime_checkable
    class Simmare(Protocol):
        def simma(self) -> str: ...

    class Anka:
        def simma(self):
            return "plask"

    assert isinstance(Anka(), Simmare) == ____


# === Final och TypeVar ===


def test_final_annotation_signals_no_reassignment():
    """Final[T] signalerar att variabeln inte ska omtilldelas — enforças av typkontrollern.
    Påverkar Final runtime-beteendet?"""
    from typing import Final
    MAX: Final[int] = 100
    MAX = 200  # runtime tillåter det — typkontrollern klagar
    assert MAX == ____
