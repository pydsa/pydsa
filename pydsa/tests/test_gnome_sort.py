from pydsa.gnome_sort import gnome_sort
from random import randint


def test_gnome_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert gnome_sort(a) == sorted(b)
