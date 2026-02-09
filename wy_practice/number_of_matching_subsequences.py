import collections
from typing import List

class TrieNode:
    def __init__(self , earliest_index=-1):
        self.children = {}
        self.earliest_index = earliest_index

class Trie:
    def __init__(self , indices):
        self.root = TrieNode()
        # cache the subsequences found to improve runtime , cache words
        # self.subsequences = set()
        # store the indices of each char
        self.indices = indices

    def find(self , key , sub_index):
        # binary search to find first > sub_index
        if key not in self.indices:
            return -1 , False
        # FFFFFFTTT
        # condition index > sub_index
        # [ 2 , 3 , 4 ] , subindex = 1

        left , right = -1 , len(self.indices[key])

        while (right - left) > 1:
            mid = (left +  right) // 2
            if self.indices[key][mid] > sub_index:
               right = mid
            else:
                left = mid

        if right == len(self.indices[key]):
            return -1 , False
        else:
            return self.indices[key][right] , True 

    def insert(self, word):
        # print("inserting word : " , word)
        curr , sub_index = self.root , -1

        for c in word:
            if c not in curr.children:
                # try to find the index of c > sub_index
                new_index , found = self.find(c , sub_index)
                if not found:
                    return False
                # insert new node with index
                new_node = TrieNode(new_index)
                curr.children[c] = new_node
            
            
            curr = curr.children[c]
            sub_index = curr.earliest_index


        return True



    def is_subsequence(self , word) -> bool:
        # check if word is a subsequence
        # can pass without the cache as well since we wont do the binary search lookup
        # if word in self.subsequences:
            # duplicate case handling 
            # return True

        # insert if possible otherwise return false
        return self.insert(word)


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        # create a mapping for character indices 
        char_indices = collections.defaultdict(list)
        for index , c in enumerate(s):
            char_indices[c].append(index)

        trie = Trie(char_indices)

        # check each word subsequence 
        for word in words:
            if trie.is_subsequence(word):
                count += 1

        return count