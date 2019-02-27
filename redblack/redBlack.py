#!/usr/bin/python
class RBNode(object):
    """
    Class for implementing the nodes that the tree will use
    For self.color:
        red == False
        black == True
        If the node is a leaf it will either
    """
    def __init__(self,data,parent):
        self.black = False
        self.red = False
        self.parent = parent
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
        """

        :param data:
        :param curr:
        :return:
        """
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
        """

        :return:
        """
        pass

    def delete(self):
        """

        :return:
        """
        pass
    def rotate_left(self):
        """

        :return:
        """
        pass
    def rotate_right(self):
        """

        :return:
        """
        pass
    def get_all_nodes(self):
        """

        :return:
        """
        pass
    def is_red(self):
        """

        :return:
        """
        return self.root != None && self.root.red == 1;
    def is_black(self):
        """
        Note that this method is not neccsary as some implementations only check is the is_red class method is True or False
        :return:
        True if the node is black or is a leaf
        """
        return self.root != None & & self.root.black == 1;


if __name__ == "__main__":
    tree = RedBlackTree()
