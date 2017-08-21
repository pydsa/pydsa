from random import randint

from pydsa.sorting.radix_sort import radix_sort


def test_radix_sort():
    """Tests Radix Sort for a randomly generated list of integers"""
    a = b = [randint(1, 100) for i in range(100)]
    assert radix_sort(a) == sorted(b)
