#!/usr/bin/python



class CharNode(object):
    """This class keeps track of if a node is at the end of the tree of possible combinations"""

    def __init__(self):
        self.end = False # this is to signal that the end pf a word has been found
        self.children = {} # this will hold a dictionary of all of the child node as a dictionary of subscriptable refrences

    def all_words_from_current_node(self, prefix):
        if self.end: # If youve reached the end of what we've defines as a word
            yield prefix # Yeet this back up the call stack and keep going

        for letter, childNodes in self.children.items(): # For all of the children of this current node
            yield from childNodes.all_words_from_current_node(prefix + letter) # Yield all possible prefixes that could exises in those nodes and r]lather, rise, repeat

