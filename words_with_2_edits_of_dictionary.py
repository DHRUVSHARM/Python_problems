from typing import List
"""
Example 1:

Input: 

queries = ["word","note","ants","wood"], 
dictionary = ["wood","joke","moat"]

                            word index ->
dictionary index            0   1   2   3
                            --------------
                            w   o   o   d
                            j   o   k   e
                            m   o   a   t


                            for q in query:
                                diff = [0 for each dict index]
                                for woi in len(q):
                                    for di in len(diff): # diff has for each di, the diff sum 
                                        if wi == 0:
                                            fix with initial values
                                            pass
                                        else:
                                            use prev 
                                            pass
                                
                                if min(diff) <= 2:
                                    append result
                                else np
                                    
                                
    
 keep running total sum of all the diff and take min of the final arr and see if <= 2 if yes put in the result    



    
wi
  
        0   0   0   0   :   0
        1   0   1   1   :   3
        1   0   1   1   :   3

    index : set() since all the words and queries are the same , if we need more than 2 then problem 

Output: ["word","note","wood"]

Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].



Example 2:

Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
 

Constraints:

1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100
All queries[i] and dictionary[j] are composed of lowercase English letters.








                            wi ->
dictionary index            0   1   2   3
                            --------------                            
                            w   o   o   d
                            j   o   k   e
                            m   o   a   t

                            for q in query:
                                diff = [0 for each dict index]
                                for woi in len(q):
                                    for di in len(diff): # diff has for each di, the diff sum 
                                        if wi == 0:
                                            fix with initial values
                                            pass
                                        else:
                                            use prev 
                                            pass
                                
                                if min(diff) <= 2:
                                    append result
                                else np                                 

                                

dfs trie 
medium 
                                


                                """



"""
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # dictionary[di][wi] # char at dictionary index di and word char wi at it 
        
        result = []
        for query_word in queries:
            diff = [0 for _ in range(len(dictionary))]
            for wi in range(len(query_word)):
                for di in range(len(dictionary)):
                    diff[di] += (1 if dictionary[di][wi] != query_word[wi] else 0)
            
            # print(diff)
            if min(diff) <= 2:
                result.append(query_word)
            
        return result
"""

# trie solution 

class TrieNode:
    def __init__(self, val=None , word_end=False):
        self.val = val
        self.children = {}
        self.word_end = word_end

class Solution:

    def insert(self, root , word):
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        
        curr.word_end = True

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        root = TrieNode() # trie

        # insert all the words into the dictionary 
        for word in dictionary:
            self.insert(root , word)
        
        # answer queries with dfs on the tree 
        def dfs(node, index, word, curr_steps):
            if index == len(word):
                if curr_steps <= 2:
                    return True
                else:
                    return False
                
            result = False
            for child in node.children.keys():
                if word[index] == child:
                    result = result or dfs(node.children[child] , index + 1 , word , curr_steps)
                elif curr_steps < 2:
                    result = result or dfs(node.children[child] , index + 1 , word, curr_steps + 1)
                if result:
                    # early exit
                    return result

            return result


        result = []
        for word in queries:
            valid = dfs(root , 0 , word, 0)
            if valid:
                result.append(word)
        

        return result