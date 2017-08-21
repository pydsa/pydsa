from random import randint

from pydsa.sorting.merge_sort import merge_sort


def test_merge_sort():
    a = [randint(1, 100) for i in range(100)]
    b = a
    assert merge_sort(a) == sorted(b)
