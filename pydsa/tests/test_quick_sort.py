from pydsa.quick_sort import *
import unittest
from random import randint


class Quick_sort(unittest.TestCase):
    """Tests for `selection_sort.py`."""

    def test_quick_sort(self):
        a = [randint(1, 100) for i in range(100)]
        b = a
        self.assertEqual(quick_sort(a), sorted(b))
