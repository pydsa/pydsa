from pydsa.binary_tree import BTNode


def test_binary_tree():
    bt = BTNode(1)
    bt.insert("left", 2)
    bt.insert("right", 3)
    bt.right.insert("left", 6)
    bt.right.insert("right", 7)
    bt.left.insert("left", 4)
    bt.left.insert("right", 5)
    bt.left.left.insert("left", 8)
    bt.left.left.insert("right", 9)

    inlist = bt.inorder(bt)
    prelist = bt.preorder(bt)
    postlist = bt.postorder(bt)

    assert inlist == [8, 4, 9, 2, 5, 1, 6, 3, 7]
    assert prelist == [1, 2, 4, 8, 9, 5, 3, 6, 7]
    assert postlist == [8, 9, 4, 5, 2, 6, 7, 3, 1]

    bt.delete(bt.left)
    bt.delete(bt.right)

    inlist = bt.inorder(bt)
    prelist = bt.preorder(bt)
    postlist = bt.postorder(bt)

    assert inlist == [8, 4, 9, 5, 1, 6, 7]
    assert prelist == [1, 5, 4, 8, 9, 7, 6]
    assert postlist == [8, 9, 4, 5, 6, 7, 1]
