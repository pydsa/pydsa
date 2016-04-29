from pydsa.binary_tree import BTNode


def test_binary_tree():
    bt = BTNode(1)
    bt.insert("left", 2)
    bt.insert("right", 3)
    bt.left.insert("left", 4)
    bt.left.insert("right", 5)
    bt.left.right.insert("left", 6)
    bt.left.right.insert("right", 7)
    bt.right.insert("right", 8)
    bt.right.right.insert("left", 9)

    inlist = bt.inorder(bt)
    prelist = bt.preorder(bt)
    postlist = bt.postorder(bt)

    assert inlist == [4, 2, 6, 5, 7, 1, 3, 9, 8]
    assert prelist == [1, 2, 4, 5, 6, 7, 3, 8, 9]
    assert postlist == [4, 6, 7, 5, 2, 9, 8, 3, 1]

    bt.left.right.delete("left")
    bt.right.delete("right")

    inlist = bt.inorder(bt)
    prelist = bt.preorder(bt)
    postlist = bt.postorder(bt)

    assert inlist == [4, 2, 5, 7, 1, 3]
    assert prelist == [1, 2, 4, 5, 7, 3]
    assert postlist == [4, 7, 5, 2, 3, 1]
