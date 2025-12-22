from typing import list 
import collections

class TrieNode:
    def __init__(self , letter = "" , frequency = 0):
        """
        letter : letter used to generate the answer
        frequency : frequency of visits
        """
        self.letter = letter
        self.frequency = 0
        self.children = collections.defaultdict(TrieNode)

    def add_child(self , letter):
       # makes a connection between the parent and the new node created
       if letter in self.children:
           return False
       child_node = TrieNode(letter , 0)
       self.children[letter] = child_node
       return True
    
    def get_child(self , letter):
        # return child
        return self.children[letter]


class Solution:
    
    def find_longest_prefix(self , root , list_size):
        ans , curr = [] , root
        
        while curr:
            next = None   
            for child in curr.children.values():
                if child.frequency == list_size:
                    ans.append(child.letter)
                    next = child
                    break
            curr = next
            
        return "".join(ans)

    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # initialize the root 
        root = TrieNode()
        
        for element in strs:
            # for the empty string
            curr = root
            curr.frequency += 1
            for letter in element:
                curr.add_child(letter)
                next = curr.get_child(letter)
                next.frequency += 1
                curr = next
            
        
        return self.find_longest_prefix(root , len(strs))