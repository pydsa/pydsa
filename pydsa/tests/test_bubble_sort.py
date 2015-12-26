from pydsa.bubble_sort import *
import unittest
from random import randint


class Bubble_sort(unittest.TestCase):
    """Tests for `selection_sort.py`."""

    def test_bubble_sort(self):
        a = [randint(1, 100) for i in range(100)]
        b = a
        self.assertEqual(bubble_sort(a), sorted(b))
