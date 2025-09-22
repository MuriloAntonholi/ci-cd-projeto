import pytest
from main import soma, subtrai, divide

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtrai():
    assert subtrai(5, 2) == 3
    assert subtrai(0, 3) == -3

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
