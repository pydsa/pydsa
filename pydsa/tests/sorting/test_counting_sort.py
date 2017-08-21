from random import randint

from pydsa.sorting.counting_sort import counting_sort


def test_counting_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert counting_sort(a, max(a)) == sorted(b)
