from pydsa.bst import BSTNode


def test_bst():
    bst = BSTNode(50)
    bst.insert(bst, 30)
    bst.insert(bst, 20)
    bst.insert(bst, 40)
    bst.insert(bst, 70)
    bst.insert(bst, 60)
    bst.insert(bst, 80)

    inlist = bst.inorder(bst)
    assert inlist == [20, 30, 40, 50, 60, 70, 80]
