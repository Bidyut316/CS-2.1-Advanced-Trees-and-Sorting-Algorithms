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


    def autocomplete(self,curr=None,word='',autocomplete_str = ''):

        if curr is None:
            curr = self.root.head

        for char in word:
            # print(curr.keys())
            if '*' in curr:
                print("eno of word")
            if char in curr:
                autocomplete_str += char
                curr = curr[char]
                print(autocomplete_str)
            # if len(curr)

    def add_to_autostring(self, add_to_auto_str='', curr_branch=None):
        # add_to_auto_str +=
        print(curr_branch)
        for letter, children in curr_branch.items():
            if letter == '*':
                add_to_auto_str += ' ' + add_to_auto_str
                yield add_to_auto_str
            else:
                # yield letter
                # print(children)
                add_to_auto_str += letter
                # yield add_to_auto_str
                yield from self.add_to_autostring(add_to_auto_str,children)


    def autocompleteTest(self, word):

        curr = self.root
        for letter in word:
            curr = cur.children.get(letter)
            if curr is None:
                return  # No words with given prefix word

        yield from curr.all_words(prefix)





if __name__ == "__main__":
    test = Autocomplete()
    # print(test.root.head)

    # print([(k,v) for k,v in {}.items()])
    test.autocompleteTest('app')