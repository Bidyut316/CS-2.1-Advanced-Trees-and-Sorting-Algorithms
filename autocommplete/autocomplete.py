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
        pprint.pprint(self.root.head)
        autocomplete_str = ''

        curr = self.root.head
        for char in word:
            print(curr.keys())
            if '*' in curr:
                print("eno of word")
            if char in curr:
                autocomplete_str += char
                print(char)
                pprint.pprint(curr[char])

                curr = curr[char]
                print(autocomplete_str)
            # if len(curr)

    # def looper(self):


    def letter_getter(self,curr_branch=None,string_of_letters=''):

        if curr_branch is None:
            curr_branch = self.root.head

        pprint.pprint(curr_branch)
        for letter in curr_branch:
            print(string_of_letters)
            if letter == '*':
                string_of_letters+= " "+string_of_letters
                continue

            else:
                if letter is not None:
                    string_of_letters += letter
                    # if curr_branch[letter]
                    yield self.letter_getter(curr_branch[letter],string_of_letters)


if __name__ == "__main__":
    test = Autocomplete()
    # print(test.root.head)

    # test.autocomplete("app")
    # print([(k,v) for k,v in {}.items()])
    print(test.letter_getter())