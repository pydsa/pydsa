from pydsa.merge_sort import *
import unittest
from random import randint


class Merge_sort(unittest.TestCase):
    """Tests for `selection_sort.py`."""

    def test_merge_sort(self):
        a = [randint(1, 100) for i in range(100)]
        b = a
        self.assertEqual(merge_sort(a), sorted(b))
