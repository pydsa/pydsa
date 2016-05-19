"""
Binary Tree
A binary tree is a hierarchial data structure in which each node has at most
two children, which are referred to as the left child and the right child.
Insertion is O(1) and deletion is O(n).
Tree traversals are O(n).
Reference used: http://geeksquiz.com/binary-search-tree-set-2-delete/
and http://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/
"""


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
    >>> bt.delete(bt.left)
    >>> bt.inorder(bt)
    [1, 3]
    """
    def __init__(self, key, left=None, right=None):
        """
        Initializes a node with value key and optionally with left and/or
        right child nodes.
        """
        self.left = left
        self.right = right
        self.key = key
        self.inlist = []
        self.prelist = []
        self.postlist = []

    def insert(self, child, key):
        """
        Takes in a string child to insert the new node with value key at left
        or right of current node.
        """
        childNode = BTNode(key)
        if child == "left":
            self.left = childNode
        elif child == "right":
            self.right = childNode

    def delete(self, root):
        self.deleteUtil(self, root)

    def deleteUtil(self, node, root):
        """
        Recursively searches sub-trees to find root (the node to be deleted).
        When found, replaces it with the child node if other is None or the
        inorder successor (and recursively deletes it) if both child nodes
        are not None.
        """
        if node is None:
            return node

        node.left = self.deleteUtil(node.left, root)
        node.right = self.deleteUtil(node.right, root)

        if node == root:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Get inorder successor of root
            temp = self.getLeftmost(root.right)
            root.key = temp.key

            # Recursively delete inorder successor
            root.right = self.deleteUtil(root.right, temp)

        return node

    def getLeftmost(self, root):
        """
        Returns the leftmost node in the tree rooted at root.
        """
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        self.inlist = []
        return self.inorderUtil(root)

    def inorderUtil(self, root):
        """
        Recursively traverses left sub-tree, then current node and then the
        right sub-tree.
        """
        if root:
            self.inorderUtil(root.left)
            self.inlist.append(root.key)
            self.inorderUtil(root.right)
        return self.inlist

    def preorder(self, root):
        self.prelist = []
        return self.preorderUtil(root)

    def preorderUtil(self, root):
        """
        Traverses the current node, then recursively traverses left sub-tree,
        and then the right sub-tree.
        """
        if root:
            self.prelist.append(root.key)
            self.preorderUtil(root.left)
            self.preorderUtil(root.right)
        return self.prelist

    def postorder(self, root):
        self.postlist = []
        return self.postorderUtil(root)

    def postorderUtil(self, root):
        """
        Recursively traverses left sub-tree, then the right sub-tree and then
        the current node.
        """
        if root:
            self.postorderUtil(root.left)
            self.postorderUtil(root.right)
            self.postlist.append(root.key)
        return self.postlist
