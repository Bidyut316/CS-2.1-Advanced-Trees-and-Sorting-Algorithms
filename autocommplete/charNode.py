#!/usr/bin/python
class CharNode(object):
    """This class keeps track of if a node is at the end of the tree of possible combinations"""
    def __init__(self, label=None, data=None):
        self.isEnd = False
        self.childNodes = dict()


    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key