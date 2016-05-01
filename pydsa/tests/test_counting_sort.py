from pydsa.counting_sort import counting_sort
from random import randint


def test_counting_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert counting_sort(a, max(a)) == sorted(b)
