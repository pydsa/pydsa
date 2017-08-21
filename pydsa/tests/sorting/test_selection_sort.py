from random import randint

from pydsa.sorting.selection_sort import selection_sort


def test_selection_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert selection_sort(a) == sorted(b)
