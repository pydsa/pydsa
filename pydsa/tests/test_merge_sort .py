from pydsa.merge_sort import merge_sort
from random import randint


def test_merge_sort():
    a = [randint(1, 100) for i in range(100)]
    b = a
    assert merge_sort(a) == sorted(b)
