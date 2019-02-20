#!/usr/bin/python
import pprint
from trie import Trie
class Autocomplete(object):
    """ This class will iplement the CharNode class to attempt to complete and autocomplete will most likely redo this in python"""
    def __init__(self):
        self.root = Trie()
        self.dictionary= [word.replace('\n', '') for word in open("/usr/share/dict/words", "r").readlines()]
        # self.dictionary =['app','apple', 'application', 'apply','apricot']
        for word in self.dictionary:
            self.root.add(word)

    def get_current_items(self):
        if "*" in self.root.head:
            yield word

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)
    def autocomplete(self,word:str):
        autocomplete_list = list()

        cur = self.root.head
        for char in word:
            cur = cur.get(char)
            if cur is None:
                return  # No words with given prefix

        yield from cur.get_current_items(word)




if __name__ == "__main__":
    test = Autocomplete()
    # test.print_current_items()