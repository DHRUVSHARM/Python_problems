from typing import List

"""

algorithm 

trie 

go through the words in wordContainer
push them in and store the min len, (min index if len is same) if no node, else put the data of len , index in 

trienode:
min len
min index
children dict size 26
we already store the nodes to have the min len, min index
so if 2 things with same letter we have what we want 
so we can just make and sort in 26 log 26

tc : 10*5 * 26 log 26 


"""


class TrieNode:
    def __init__(self , min_len=float("inf") , min_index=float("inf")):
        self.min_len = min_len
        self.min_index = min_index
        self.children = {}


class Solution:

    def insert(self, root , word , word_len , word_index):
        curr = root

        # find the minimal and keep the earlier index if the lengths are equal 
        if curr.min_index == float("inf") or word_len < curr.min_len:
            # clear update if one is less than the other or first entry  
            curr.min_len = word_len
            curr.min_index = word_index
        elif word_len == curr.min_len:
            # earlier index 
            curr.min_index = min(curr.min_index , word_index)
        else:
            # reject, no update 
            pass

        # print("word : " , word)
        # print("min_index at root : " , curr.min_index)
        # print("min word len at root : " , curr.min_len)

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(word_len , word_index)
            else:
                # find the minimal and keep the earlier index if the lengths are equal 
                if curr.children[c].min_index == float("inf") or word_len < curr.children[c].min_len:
                    # clear update if one is less than the other or first entry  
                    curr.children[c].min_len = word_len
                    curr.children[c].min_index = word_index
                elif word_len == curr.children[c].min_len:
                    # earlier index 
                    curr.children[c].min_index = min(curr.children[c].min_index , word_index)
                else:
                    # reject, no update 
                    pass

            curr = curr.children[c]
        # it is required to keep inserting the full thing since we need to match longest suffixes 

    
    def match(self, root, word):
        curr = root
        # print(word)

        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
        
        # print(curr.min_index)
        return curr.min_index


    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        rev_w , rev_q = [] , []

        # suffix tree 
        for word in wordsContainer:
            word = word[::-1]
            rev_w.append(word)
        
        for query in wordsQuery:
            query = query[::-1]
            rev_q.append(query)

        for index, word in enumerate(rev_w):
            # insert word in trie with imp information 
            self.insert(root , word, len(word) , index)

        res = []
        for query in rev_q:
            res.append(self.match(root, query))
    
        return res