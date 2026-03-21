# implementation and trie theory 
"""
used to search common prefixes
used to perform ops where we need to think about common prefixes 

prefix tree - trie 
suffix tree 

trie allows partial matching 

try to think about the letters on the edges 

root ""

a   b   c   ...

"""

# children maps the key to the trienode  
# word , denotes the ending of the word
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

# going to give us the interface to handle the different operations on the trie
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # all ops are o word time 
    
    def insert(self , word):
        """
        traverse and insert if needed 
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.word = True
    
    def search(self , word)->bool:
        """
        search for the given word, return true if found else false 
        note : we need to make sure that the word exists, just the prefix finding is not enough
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                # that the word is not there 
                return False
            curr = curr.children[w]
        
        return curr.word

    def starts_with(self , prefix)->bool:
        """
        starts with the prefix prefix 
        """
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        
        return True