# Binary Tree
# A binary tree is a hierarchial data structure in which each node has at most
# two children, which are referred to as the left child and the right child.
# Insertion and deletion are O(1)
# Tree traversals are O(n)


class BTNode(object):
    """
    Class to create a Binary Tree Node, insert, delete child nodes and
    print inorder, preorder and postorder traversals.

    >>> from pydsa import binary_tree
    >>> bt = binary_tree.BTNode(1)
    >>> bt.insert("left", 2)
    >>> bt.insert("right", 3)
    >>> bt.inorder(bt)
    [2, 1, 3]
    >>> bt.preorder(bt)
    [1, 2, 3]
    >>> bt.postorder(bt)
    [2, 3, 1]
    >>> bt.delete("left")
    >>> bt.inorder(bt)
    [1, 3]
    """
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.inlist = []
        self.prelist = []
        self.postlist = []

    def insert(self, child, key):
        childNode = BTNode(key)
        if child == "left":
            self.left = childNode
        elif child == "right":
            self.right = childNode

    def delete(self, child):
        if child == "left":
            self.left = None
        elif child == "right":
            self.right = None

    def inorder(self, root):
        self.inlist = []
        return self.inorderUtil(root)

    def inorderUtil(self, root):
        if root:
            self.inorderUtil(root.left)
            self.inlist.append(root.key)
            self.inorderUtil(root.right)
        return self.inlist

    def preorder(self, root):
        self.prelist = []
        return self.preorderUtil(root)

    def preorderUtil(self, root):
        if root:
            self.prelist.append(root.key)
            self.preorderUtil(root.left)
            self.preorderUtil(root.right)
        return self.prelist

    def postorder(self, root):
        self.postlist = []
        return self.postorderUtil(root)

    def postorderUtil(self, root):
        if root:
            self.postorderUtil(root.left)
            self.postorderUtil(root.right)
            self.postlist.append(root.key)
        return self.postlist
