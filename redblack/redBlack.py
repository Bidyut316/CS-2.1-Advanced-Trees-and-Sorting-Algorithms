#!/usr/bin/python
class RBNode(object):
    """
    Class for implementing the nodes that the tree will use
    For self.color:
        red == False
        black == True
        If the node is a leaf it will either
    """
    def __init__(self,data):
        self.black = False
        self.data = data
        self.left = None
        self.right = None

class RedBlackTree(object):
    """
    Class for implementing a standard red-black trees
    """
    def __init__(self,data):
        self.root = RBNode(data)
        self.root.black = True

    def add(self,data,curr = None):
        if not curr :
            curr = self.root
        if data > curr.data:
            if curr.right is None:
                curr.right = RBNode(data)
            else:
                pass
                # while curr.right is not None:

        if data < curr.data:
            if curr.left is None:
                curr.left = RBNode(data)
        pass
    def contain(self):
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


if __name__ == "__main__":
    tree = RedBlackTree()
