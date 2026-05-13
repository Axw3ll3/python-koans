from sentinel import ____


# === Unika element och mängdoperationer ===


def test_set_discards_duplicates():
    """Set lagrar bara unika element — dubbletter kastas bort tyst.
    Vad är len({1, 2, 2, 3})?"""
    assert len({1, 2, 2, 3}) == ____


def test_union_contains_all_elements_from_both_sets():
    """| returnerar en ny mängd med alla element från båda mängderna.
    Vad är {1, 2, 3} | {3, 4}?"""
    assert {1, 2, 3} | {3, 4} == ____


def test_intersection_contains_only_shared_elements():
    """& returnerar elementen som finns i *båda* mängderna.
    Vad är {1, 2, 3} & {2, 3, 4}?"""
    assert {1, 2, 3} & {2, 3, 4} == ____


def test_difference_removes_shared_elements_from_left():
    """- returnerar elementen som finns i vänster mängd men inte i höger.
    Vad är {1, 2, 3} - {2, 3}?"""
    assert {1, 2, 3} - {2, 3} == ____


# === Fallgrop: set stöder inte indexering ===


def test_sets_do_not_support_index_access():
    """Set har ingen garanterad ordning och stöder inte indexering.
    Vilken exception kastar {1, 2, 3}[0]?"""
    import pytest
    with pytest.raises(____):
        _ = {1, 2, 3}[0]


# === add, frozenset och ordning ===


def test_add_method_inserts_one_element():
    """add() lägger till ett enskilt element i ett set.
    Är 3 i s efter s.add(3)?"""
    s = {1, 2}
    s.add(3)
    assert (3 in s) == ____


def test_frozenset_is_an_immutable_set():
    """frozenset är ett immutabelt set — kan användas som dict-nyckel.
    Vad är typen av frozenset({1, 2})?"""
    assert type(frozenset({1, 2})) == ____


def test_equal_sets_regardless_of_creation_order():
    """Set jämförs efter innehåll, inte ordning. Är {3, 1, 2} == {1, 2, 3}?"""
    assert ({3, 1, 2} == {1, 2, 3}) == ____
