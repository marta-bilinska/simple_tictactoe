"""This module contains"""


class Node:
    """This class defines a node"""
    def __init__(self, right, left):
        """
        node, node -> ()
        Initializes a node object.
        """
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
