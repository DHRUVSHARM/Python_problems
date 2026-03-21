from typing import List

"""

observations :
Users may input a sentence (at least one word and end with a special character '#').
sentences, times size : n

AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love neetcode"], [5, 3, 2, 2]);

problem is easy since the python under the hood comparision is based on ascii


c is a lowercase English letter, a hash '#', or space ' '.


            "" empty space  
        
            i at every node, we will store all the sentences that have passed this point  ( for the initial processing ) 


            
            
trienode
    prefix : inital string
    children : dict key -> node
    sentences = [] default store the senetence passinmg through (freq , sentence)

    
autocomplete
    state 
        current node : root  store the root currently being explored to add
        current sentence : "" store the sentence being explored to add
             
# init :
1) for each sentence insert character by character
    can use the current node state and insert can be to add as a child 
2) then populate the sentence down the path (basically from "" until the end character, just add the (freq , sentence) as metadata)


# find 
if c is not # 
    we can just have a find function that will get us to the matched char (prefix) and if this is not found we can create and return empty (default anyway)  
    we can store the current pointed node as well ,
    the insert can be using the given node and an insert 
if # we store for future context
    tou wont find, so return the [] and to store with freq = 1 , sentence = currsentence, and reset
    we will store the current sentence as state in the class since it is a stateful thing 
    reset to the root, once done 

# we add the word character by character , need to insert it, if the character does not exist



helper : that will take the sentence and populate each node on the path 

"""
import collections

class TrieNode:
    def __init__(self , prefix=""):
        self.prefix = prefix
        self.children = collections.defaultdict()
        self.sentences = [] # sentences passing through
        self.freq = collections.defaultdict() # in case the same sentence is to be added again we can redo the sentences list 

class Trie:
    def __init__(self):
        # new root 
        self.root = TrieNode()
    
    def insert_character(self, curr_node, c):
        """
        add c as a child of the curr_node
        and return the sentences at this point , we will use it for the other case also 
        """
        curr = curr_node
        if c not in curr.children:
            curr.children[c] = TrieNode(c)
        # we have the curr child in the trie
        return curr.children[c].sentences
    
    def insert_sentence(self, sentence , frequency):
        """
        insert the sentence from the root to the end at each character
        if the sentence already exists, we can update the frequency and recompute 
        the sentences metadata 
        """
        curr = self.root
        for c in sentence:
            curr = curr.children[c] # we know it exist and can move
            if sentence in curr.freq:
                # need to update 
                curr.freq[sentence] += frequency
                # recompute the sentences stored make copy since it may need to be updated 
                curr.sentences = [(f , s) for s , f in curr.freq.items()]
            else:
                # simple append with the freq and update
                curr.freq[sentence] = frequency
                curr.sentences.append((frequency , sentence))
            

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # state
        self.trie = Trie() # trie to manage the prefixes
        self.curr_node = self.trie.root 
        self.curr_sentence = [] # we will use list to store the sentence and join when needed 

        # need to process the sentences and the times initially 
        for sentence , time in zip(sentences , times):
            # insert char by char
            for c in sentence:
                self.trie.insert_character(self.curr_node , c)
                # move the node
                self.curr_node = self.curr_node.children[c]
                # update sentence currently used 
                self.curr_sentence.append(c)

            # once done we can also add the complete sentence to the path created as metadata 
            self.trie.insert_sentence("".join(self.curr_sentence) , time)
            
            # reset for next sentence 
            self.curr_node = self.trie.root
            self.curr_sentence = []

    def input(self, c: str) -> List[str]:
        # need to handle the # and other case separately
        if c == '#':
            # the sentence is complete and we need to store the senetence metadata in the trie 
            self.trie.insert_sentence("".join(self.curr_sentence) , 1) # single frequency
            self.curr_sentence = []
            self.curr_node = self.trie.root
            return []
        else:
            # we need to insert the character
            self.trie.insert_character(self.curr_node , c)
            # advance to the current node and add to the curr sentence 
            self.curr_node = self.curr_node.children[c]
            self.curr_sentence.append(c)
            # we need to return the sentences matched, top 3, all if less, in order of hot and alphabetical 
            sentences = self.curr_node.sentences
            # max freq, min sentence order 
            sentences.sort(key=lambda x : (-x[0] , x[1]))
            sentences = sentences[:3]        
            return [s for (f , s) in sentences]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
