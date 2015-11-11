from pydsa.bst import *
import unittest


class BSTTestCase(unittest.TestCase):
    """Tests for `bst.py`."""

    def test_is_five_prime(self):
        bst = BSTNode(50)
        bst.insert(bst, 30)
        bst.insert(bst, 20)
        bst.insert(bst, 40)
        bst.insert(bst, 70)
        bst.insert(bst, 60)
        bst.insert(bst, 80)

        inlist = bst.inorder(bst)
        self.assertEqual(inlist, [20, 30, 40, 50, 60, 70, 80])