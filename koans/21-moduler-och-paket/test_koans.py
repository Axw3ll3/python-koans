from sentinel import ____


# === __name__ och __main__ ===


def test_imported_module_name_is_not_main():
    """__name__ är "__main__" när filen körs direkt med `python fil.py`.
    När filen importeras sätts __name__ i stället till modulens eget namn.
    Vad är __name__ för sys-modulen när den importeras?"""
    import sys
    assert sys.__name__ == ____


def test_imported_module_has_its_module_name():
    """En importerad modul har sitt eget filnamn som __name__.
    Vad är math.__name__ efter import math?"""
    import math
    assert math.__name__ == ____


# === import och namnrymder ===


def test_from_import_brings_name_into_local_namespace():
    """from math import sqrt importerar sqrt direkt till det lokala scopet.
    Vad är typen av path efter from os import path?"""
    from os import path
    import types
    assert type(path) == ____


def test_import_as_creates_an_alias():
    """import math as m skapar aliaset m — math.pi nås via m.pi.
    Vad returnerar m.pi (avrundat till 2 decimaler)?"""
    import math as m
    assert round(m.pi, 2) == ____


def test_init_py_marks_a_directory_as_a_package():
    """__init__.py gör en katalog till ett Python-paket — den kan vara tom.
    Är collections ett paket eller en modul?"""
    import collections, types
    assert type(collections) == ____


# === Cirkulär import och sys.path ===


def test_sys_path_is_a_list():
    """sys.path är listan med kataloger Python söker igenom vid import.
    Vilken typ är sys.path?"""
    import sys
    assert type(sys.path) == ____
