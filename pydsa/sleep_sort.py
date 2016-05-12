from time import sleep
from threading import Timer


# Sleep Sort ;)
# Complexity: O(max(input)+n)


def sleep_sort(a):
    """
    Sorts the list 'a' using Sleep sort algorithm

    >>> from pydsa import sleep_sort
    >>> a = [3, 4, 2]
    >>> sleep_sort(a)
    [2, 3, 4]

    """
    sleep_sort.result = []

    def add1(x):
        sleep_sort.result.append(x)

    mx = a[0]
    for v in a:
        if mx < v:
            mx = v
        Timer(v, add1, [v]).start()
    sleep(mx + 1)
    return sleep_sort.result
