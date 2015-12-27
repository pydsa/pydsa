from pydsa.insertion_sort import insertion_sort
from random import randint


def test_insertion_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert insertion_sort(a) == sorted(b)
