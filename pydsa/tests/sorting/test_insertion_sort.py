from random import randint

from pydsa.sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert insertion_sort(a) == sorted(b)
