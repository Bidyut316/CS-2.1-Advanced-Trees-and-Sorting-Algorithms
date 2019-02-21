
import pprint
from charNode import CharNode
class Trie:
    def __init__(self):
        self.root = CharNode()


                # this represents the starting point for searching, adding, or removing words or sentences,
                # it store a reference to the starting letter to track down ( in later methods like add or search)
                # each letter that is seen will hold a dictionary of letters that reference other letters,
                # based on the add _method has added to the dictionary,



    def add(self, word):
        """
        This add function takes pythons iterating over a list of keys as the for loop that it checks for each letter in the word trees dictionary
        For out first example, let's add the word "add" to the Trie
        I'd first have to define the Trie as an empty dictionary as defined as self.head being  {}

                        testTree = Trie()




        Adding "add" to the Trie
         We're going to drop in the string "add" to the Trie via the Trie.add() method
                        Test

        First we define a variable curr as the self.head so we can "creep down the tree" att every level and check its keys

        lets start at the letter "a" for the forth coming for loop
        It checks to see if "a" is a key at the first level, which would be the self.head at this point and is empty
        We would then add "a" to the top level self.head dictionary resulting in the following
                        self.head = {
                                    "a"
                                }
        What we also need to do is give the "a" key a value that we can store letters that come after it in the word
        In this case another empty dictionary

                        self.root = {

                                    "a":{}
                                    }

        We will now set "a"'s dictionary as the current value we'll check keys.
        The next  iteration of the for loop now puts us at the letter "d"
                and puts the curr that were on to "a"s empty dictionary

                        "a":{}


          # example if I've only added the words "add", addiction" and "apple","apply" the resulting dictionary would look like

                    # "a" : {
    #                           "d": {
    #                                   "d": {
    #                                           "i": {
    #                                                     "c": {
    #                                                          "t": {
    #                                                                   "i" : {
    #                                                                           "o": {
    #
    #                                                                                   "n": {


                                                                                            }
    #
    #
    #                                                                                   },
    #
    #
    #                                                                   },
    #                                                          },
    #
    #
    #                                           },
    #
    #
    #                                       }
    #
    #                                   },

    #                           "p": {
    #
    #                           }
    #                        }

    we know that ever time we find and empty dictionary that the word has ended.

     if theres still more letters in the  word that were searching for we know its not in the dictionary. will be in the search


        :param word: A string that we want to add its letter references to the current tree
        :return: Nothing, but modifies self. head with new charNode entries
        """

        curr = self.root
        for ch in word: # For every character in the word that we are trying adding to the trie-node reference
            node = curr.children.get(ch) # Check to see if the character is in the dictionary of children Charnodes
            if not node: # If it comes back that there is no child with that key
                node = CharNode() # Declare the  node as a new charnode
                curr.children[ch] = node # creep down to the nest lever of the trie and continue until word is added
            curr = node
        curr.end = True # This sets to true for the sole purpose of the next few methods win which this determines the end of a word



    def search(self, search_word):
        if len(self.root.children) =={}:
            raise ValueError(" The dictionary is empty, please add words via the add method")
        curr = self.root
        for letter in search_word: #loop over every letter in the word that we're searching in
            node = curr.children.get(letter) #attempt to see if the letter is in thechildren of this trie level
            if not node: # if the letter isnt represented in the trie
                return False # return false as it means this word doesnt exist in the trie
            curr = node # creep down to the next level of the trie
        return curr.end




if __name__ == "__main__":
        trieTest = Trie()
        print(trieTest.root.children)
        # trieTest.search("word")
        trieTest.add("add")
        # pprint.pprint(trieTest.head)
        trieTest.add("addiction")
        # pprint.pprint(trieTest.head)
        print(trieTest.search("add"))


