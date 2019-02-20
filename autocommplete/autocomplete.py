#!/usr/bin/python
import pprint
from trie import Trie
class Autocomplete(object):
    """ This class will iplement the CharNode class to attempt to complete and autocomplete will most likely redo this in python"""
    def __init__(self):
        self.root = Trie()
        # self.dictionary= [word.replace('\n', '') for word in open("/usr/share/dict/words", "r").readlines()]
        self.dictionary =['app','apple', 'application', 'apply','apricot']
        for word in self.dictionary:
            self.root.add(word)


    def autocomplete(self,word:str):
        autocomplete_list = list()

        curr = self.root.head
        for char in word:
            print(curr.values())
            if not curr: # checking to see if the current dictionary that were in isnt just an empty dict
                return  # No words with given prefix, aka these letters do not appear




if __name__ == "__main__":
    test = Autocomplete()
    # print(test.root.head)
    # test.autocomplete("app")
    print([(k,v) for k,v in {}.items()])