#!/usr/bin/python

class NilNode(object):
    """
    The nil class is specifically for balancing a tree by giving all  traditional leaf noes tw children that are null
     and waiting to be filled
    """
    def __init__(self):
        self.red = False


NIL = NilNode() # Nil is the sentinel value for nodes


class RBNode(object):
    """
    Class for implementing the nodes that the tree will use
    For self.color:
        red == False
        black == True
        If the node is a leaf it will either
    """
    def __init__(self,data):
        self.red = False
        self.parent = None
        self.data = data
        self.left = None
        self.right = None

class RedBlackTree(object):
    """
    Class for implementing a standard red-black trees
    """
    def __init__(self,data):
        self.root = None
        self.root.black = True

    def add(self,data,curr = None):
        """

        :param data:
        :param curr:
        :return: None but midifies tree to have an additional node
        """
        newNode= RBNode(data)
        curr = self.root
        while curr !=NIL:
            if newNode.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        newNode.parent = curr
        if curr == None:
            self.root = newNode
        elif newNode.data < curr.data:
            curr.left = newNode
        else:
            curr._right = newNode
        newNode.left =NIL
        newNode.right =NIL
        newNode.red = True
        self.fix_tree_after_add(newNode)

    def contains(self,data, curr=None):
        """

        :return:
        """
        if curr == None:
            curr = self.root
        while curr != NIL and data != curr.key:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def fix_tree_after_add(self):
        """
        This method is meant to check that a treee is still balances after and insertion and perform the neccesary left
        or right rotations as defined by the methods below

        :return:
        None, but modifiex tree
        """

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
        This is the class that usually decides that a node is wither red or black, some implementations take the ecurrtra
        bit and will implement an is_black method for additional clarity.
        Generally, True == Red and False == Black

        :return:
        """
        return self.root != None && self.root.red == 1;
    def is_black(self):
        """
        Note that this method is not necessary as some implementations only check is the is_red class method is True or False
        :return:
        True if the node is black or is a leaf
        """
        return self.root != None & & self.root.black == 1;


if __name__ == "__main__":
    tree = RedBlackTree()
