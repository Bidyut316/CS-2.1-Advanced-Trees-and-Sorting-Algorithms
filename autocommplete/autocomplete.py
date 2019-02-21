#!/usr/bin/python

from trie import Trie
class Autocomplete(object):
    """ This class will iplement the CharNode class to attempt to complete and autocomplete will most likely redo this in python"""
    def __init__(self):
        self.root = Trie()
        self.dictionary= [word.replace('\n', '') for word in open("/usr/share/dict/words", "r").readlines()]
        # self.dictionary =['app','apple', 'application', 'apply','apricot']
        for word in self.dictionary:
            self.root.add(word)



    def autocompleteTest(self, word):

        curr = self.root.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                return  # No words with given prefix word

        yield from curr.all_words_from_current_node(word)





if __name__ == "__main__":
    test = Autocomplete()
    # print(test.root.head)

    # print([(k,v) for k,v in {}.items()])
    for word in test.autocompleteTest('app'):
       print(word)