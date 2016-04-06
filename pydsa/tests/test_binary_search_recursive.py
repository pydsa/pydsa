from pydsa.binary_search import binary_search
from random import randint

def test_binary_search_recursive():
    a = [randint(1, 10) for i in range(10)]
    item = randint(1, 10)
    a = sorted(a)
    ans1 = binary_search(a, item, True)
    ans2 = binary_search(a, item, True, 0, len(a) - 1)
    if(ans1 == ans2 == -1):
        assert item not in a
    else:
        assert a[ans1] == item == a[ans2]
