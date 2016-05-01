from pydsa.sleep_sort import sleep_sort
from random import randint


def test_sleep_sort():
    a = b = [randint(1, 3) for i in range(3)]
    assert sleep_sort(a) == sorted(b)
