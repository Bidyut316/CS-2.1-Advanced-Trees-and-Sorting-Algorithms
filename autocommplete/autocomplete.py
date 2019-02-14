#!/usr/bin/python
from charNode import CharNode
class Autocomplete(object):
    """ This class will iplement the CharNode class to attempt to complete and autocomplete will most likely redo this in python"""
    def __init__(self):
        self.root = CharNode()
        self.dictionary= [word.replace('\n', '') for word in open("/usr/share/dict/words", "r").readlines()]



if __name__ == "__main__":
    test = Autocomplete()
    print(test.dictionary)