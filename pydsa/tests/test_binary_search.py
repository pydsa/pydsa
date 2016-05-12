from pydsa.binary_search import binary_search
from random import randint


def test_binary_search():
    a = [randint(1, 10) for i in range(10)]
    item = randint(1, 10)
    a = sorted(a)
    ans = binary_search(a, item)
    if (ans == -1):
        assert item not in a
    else:
        assert a[ans] == item


def test_binary_search_recursive():
    a = [randint(1, 10) for i in range(10)]
    item = randint(1, 10)
    a = sorted(a)
    ans_through_method_1 = binary_search(a, item, True)
    ans_through_method_2 = binary_search(a, item, True, 0, len(a) - 1)
    if (ans_through_method_1 == ans_through_method_2 == -1):
        assert item not in a
    else:
        assert a[ans_through_method_1] == item == a[ans_through_method_2]
