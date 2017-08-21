from pydsa import bubble_sort
from random import randint


def test_bubble_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert bubble_sort(a) == sorted(b)
