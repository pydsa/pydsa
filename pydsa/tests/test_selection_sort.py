from pydsa.selection_sort import *
import unittest
from random import randint


class Selection_sort(unittest.TestCase):
    """Tests for `selection_sort.py`."""

    def test_selection_sort(self):
        a = [randint(1, 100) for i in range(100)]
        b = a
        self.assertEqual(selection_sort(a), sorted(b))
