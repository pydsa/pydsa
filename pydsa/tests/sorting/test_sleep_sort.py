from random import randint

from pydsa.sorting.sleep_sort import sleep_sort


def test_sleep_sort():
    a = b = [randint(1, 3) for i in range(3)]
    assert sleep_sort(a) == sorted(b)
