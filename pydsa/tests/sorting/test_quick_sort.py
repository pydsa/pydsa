from random import randint

from pydsa.sorting.quick_sort import quick_sort


def test_quick_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert quick_sort(a) == sorted(b)
