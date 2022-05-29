import pytest

from openpack_toolkit.utils.notebook import noglobal


def test_noglobal__01():
    a = 10
    b = 20

    @noglobal()
    def func():
        c = 30
        return c

    assert a == 10
    assert b == 20
    assert func() == 30


def test_noglobal__02():
    a = 10
    b = 20

    @noglobal()
    def func():
        c = a + b
        b = 25
        return c

    assert a == 10
    assert b == 20
    with pytest.raises(UnboundLocalError):
        func()
