class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False 

# trie manages the trienode
class Trie:
    def __init__(self):
        self.root =  TrieNode()

    def insert(self , word) -> None:
        # insert a word into the trie
        curr = self.root
        for index in range(0 , len(word)):
            # in our case we map the char to the child node
            # "" -> a -> b
            if word[index] not in curr.children:
                child_node = TrieNode()
                curr.children[word[index]] = child_node
            curr = curr.children[word[index]]
        curr.word_end = True

    def search(self , word) -> bool:
        # will return if word is found in the current corpus
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        # extra check 
        return True if curr.word_end else False

    def startswith(self , prefix) -> bool:
        # we need to check if the tree contains a certain prefix
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True