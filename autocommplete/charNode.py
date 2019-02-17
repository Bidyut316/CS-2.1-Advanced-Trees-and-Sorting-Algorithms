#!/usr/bin/python



def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


class CharNode(object):
    """This class keeps track of if a node is at the end of the tree of possible combinations"""

    def __init__(self):
        self.next = dict() # Initialize and empty python dictionary that will hold references to

        self.word_marker = False
