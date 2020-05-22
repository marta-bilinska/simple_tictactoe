"""This module contains a tree class"""


class Tree:
    """
    This class defines a tree.
    """
    def __init__(self, root, right=None, left=None):
        self.root = root
        self.right = right
        self.left = left

    def get_right(self):
        """
        self -> node
        Gets right child.
        """
        return self.right

    def get_left(self):
        """
        self -> node
        Gets left child.
        """
        return self.left
