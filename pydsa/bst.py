# Binary Search Tree
# Create a BST and insert elements and print Inorder traversal


class BSTNode(object):
    """
    Class to create a Binary Search Tree Node.
    """
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.inlist = []

    def insert(self, node, key):
        if node is None:
            return BSTNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inlist.append(root.key)
            self.inorder(root.right)
        return self.inlist

if __name__ == "__main__":
    bst = BSTNode(50)
    bst.insert(bst, 30)
    bst.insert(bst, 20)
    bst.insert(bst, 40)
    bst.insert(bst, 70)
    bst.insert(bst, 60)
    bst.insert(bst, 80)

    inlist = bst.inorder(bst)
    print(inlist)
