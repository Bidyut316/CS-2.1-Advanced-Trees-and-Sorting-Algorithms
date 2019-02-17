
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
class Trie:
    def __init__(self):
        return

    head = {}
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

                        self.head = {

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
        :return: Nothing, but modifies self. head with new dictonary entries
        """

        curr = self.head

        for ch in word: #For every character in the word that we are trying adding to the dictionary
            if ch not in curr: #Iterate over the list of keys in self.head/ the current dictionary were on and if the character isnt in the keys
                curr[ch] = {}   # we add it as another  dictionary
                print(curr)  # Check to see the current dictionary were on and what keys it has
            curr = curr[ch]  #  Either way check for the next iteration of the for loop it wil now reference
        curr["*"]= True


    def search(self, search_word):
        if len(self.head) ==0:
            raise ValueError(" The dictionary is empty, please ass words via the add method")

        curr = self.head
        for char in search_word:
            if char not in curr:
                return False # this will short circut and return early if, for this iteration, the character is not in the keys
            curr = curr[char]   # if it is in the keys then for the nest letter its curr will be a list of keys that it was found
                                # having dropped into its dictionary via the add method


if __name__ == "__main__":
        trieTest = Trie()
        print(trieTest.head)
        trieTest.search("word")
