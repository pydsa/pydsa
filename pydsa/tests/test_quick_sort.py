from pydsa.quick_sort import quick_sort
from random import randint


def test_quick_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert quick_sort(a) == sorted(b)
