from pydsa.insertion_sort import *
import unittest
from random import randint


class Insertion_sort(unittest.TestCase):
    """Tests for `selection_sort.py`."""

    def test_insertion_sort(self):
        a = [randint(1, 100) for i in range(100)]
        b = a
        self.assertEqual(insertion_sort(a), sorted(b))
