from pydsa.sleep_sort import *
from random import randint


def test_sleep_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert sleep_sort(a) == sorted(b)
