from sentinel import ____


# === Arv och isinstance ===


def test_subclass_instance_is_also_instance_of_parent():
    """isinstance kontrollerar hela arvshierarkin — inte bara direkt typ.
    Är B() en instans av A om class B(A)?"""
    class A:
        pass
    class B(A):
        pass
    assert isinstance(B(), A) == ____


def test_isinstance_is_true_for_indirect_inheritance():
    """isinstance() är True oavsett hur djupt i hierarkin instansen befinner sig.
    Är C() en instans av A om class C(B) och class B(A)?"""
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass
    assert isinstance(C(), A) == ____


def test_issubclass_checks_the_class_hierarchy():
    """issubclass(B, A) är True om B ärver från A — direkt eller indirekt.
    Är issubclass(B, A) True när class B(A)?"""
    class A:
        pass
    class B(A):
        pass
    assert issubclass(B, A) == ____


# === MRO och super() ===


def test_mro_starts_with_the_class_itself():
    """__mro__ listar klassen och alla dess föräldrar i uppslagsordning.
    Är B den första klassen i B.__mro__?"""
    class A:
        pass
    class B(A):
        pass
    assert B.__mro__[0] == ____


def test_subclass_method_overrides_parent_method():
    """En metod i subklassen med samma namn skuggar förälderns metod.
    Vad returnerar b.hälsa() om B.hälsa returnerar "B" och A.hälsa returnerar "A"?"""
    class A:
        def hälsa(self):
            return "A"
    class B(A):
        def hälsa(self):
            return "B"
    b = B()
    assert b.hälsa() == ____


def test_super_calls_parent_method():
    """super() delegerar anropet till nästa klass i MRO.
    Vad returnerar b.hälsa() om B.hälsa gör "B + " + super().hälsa()?"""
    class A:
        def hälsa(self):
            return "A"
    class B(A):
        def hälsa(self):
            return "B + " + super().hälsa()
    b = B()
    assert b.hälsa() == ____


# === Multipelt arv ===


def test_multiple_inheritance_mro_left_to_right():
    """Vid multipelt arv (class C(A, B)) söks metoderna i MRO-ordning från vänster.
    Vilken förälderklass metod anropas via super() om A och B båda har metoden?"""
    class A:
        def metod(self):
            return "A"
    class B:
        def metod(self):
            return "B"
    class C(A, B):
        pass
    assert C().metod() == ____
