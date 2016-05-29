from pydsa.heap_sort import heap_sort
from random import randint

def test_heap_sort():
    a = [randint(1, 10) for i in range(10)]
    b = sorted(a)
    heap_sort(a)
    assert a == b

