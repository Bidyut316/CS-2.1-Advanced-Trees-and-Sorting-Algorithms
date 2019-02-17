#!/usr/bin/python
from charNode import CharNode
class Autocomplete(object):
    """ This class will iplement the CharNode class to attempt to complete and autocomplete will most likely redo this in python"""
    def __init__(self):
        self.root = CharNode()
        # self.dictionary= [word.replace('\n', '') for word in open("/usr/share/dict/words", "r").readlines()]
        self.dictionary =['app','apple', 'application', 'apply','apricot']
    def get_possisble_words(self,word:str):
        for word in self.dictionary:
            print(word)
        print(type(self.root))
        



if __name__ == "__main__":
    test = Autocomplete()
    print(test.root.children)