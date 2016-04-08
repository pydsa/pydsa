from pydsa.binary_search import binary_search
from random import randint

def test_binary_search():
    a = [randint(1, 10) for i in range(10)]
    item = randint(1, 10)
    a = sorted(a)
    ans = binary_search(a, item)
    if(ans == -1): 
        assert item not in a
    else: 
        assert a[ans] == item
