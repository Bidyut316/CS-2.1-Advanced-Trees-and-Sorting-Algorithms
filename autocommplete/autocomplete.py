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

    # def looper(self):
    def add_to_autostring(self,add_to_auto_str = '',curr_branch=None):
        # add_to_auto_str +=
        for letter, children in curr_branch.items():
            add_to_auto_str += letter
            print(add_to_auto_str)
            print(letter)
            print(children)

    def autocompleteTest(self,word='',autocomplete_str = '',curr=None):

        if curr is None:
            curr = self.root.head

        # if word[0] not in curr:
        #     print('Not in here')
        for letter in word:
            autocomplete_str +=letter
            if letter not in curr:
                print('Not Found')
                break
            curr= curr[letter]
        self.add_to_autostring(autocomplete_str, curr)
        print(autocomplete_str)



    def letter_getter(self,curr_branch=None,string_of_letters=''):

        if curr_branch is None:
            curr_branch = self.root.head

        pprint.pprint(curr_branch)
        for letter in curr_branch:
            print(string_of_letters)
            if letter == '*':
                # string_of_letters += " " + string_of_letters
                print(string_of_letters)

            if letter != '*':
                string_of_letters += letter
                self.letter_getter(curr_branch[letter], string_of_letters)

            # string_of_letters += letter



if __name__ == "__main__":
    test = Autocomplete()
    # print(test.root.head)

    # print([(k,v) for k,v in {}.items()])
    test.autocompleteTest('apr')