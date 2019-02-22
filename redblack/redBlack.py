#!/usr/bin/python
class RBNode(object):
    """
    Class for implementing the nodes that the tree will use
    """
    def __init__(self):
        self.color=''
        self.left = None
        self.right = None

class RedBlackTree(object):
    """
    Class for implementing a standard red-black trees
    """
    def __init__(self):
        self.root =RBNode()

    def add(self):
        pass
    def delete(self):
        pass
    def rotate_left(self):
        pass
    def rotate_right(self):
        pass
    def get_all_nodes(self):
        pass
    def get_red_nodes(self):
        pass
    def get_black_nodes(self):
        pass