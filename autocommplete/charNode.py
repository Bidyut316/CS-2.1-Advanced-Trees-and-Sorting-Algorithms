#!/usr/bin/python



class CharNode(object):
    """This class keeps track of if a node is at the end of the tree of possible combinations"""

    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end: # If youve reached the end of what we've defines as a word
            yield prefix # Yeet this back up the call stack and keep going

        for letter, childNodes in self.children.items(): # For all of the children of this current node
            yield from childNodes.all_words(prefix + letter) # Yield all possible prefixes that could exises in those nodes and r]lather, rise, repeat

