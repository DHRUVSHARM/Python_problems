from typing import List

"""
You receive a list of non-empty
 strings words from the dictionary,
   where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language.
If the order is invalid, return an empty string.
If there are multiple valid order of letters, return any of them.

ex 

Input: ["hrn","hrf","er","enn","rfnn"]

h           e   
r       f       n
n           r   

Output: "hernf"

iterate through the words
only adjacent consideration is enough

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100

build graph
do dfs to check cycle / order


1) so we can infer only the first point of diff

The first letter where they differ is smaller in a than in b.


a is a prefix of b and a.length < b.length. - this does not really give any info 

inc lex
return empty if dag

topo sort dfs

will return reverse


"hrn","hrf","er



a   b   c       

key issues, 
transititbity proof
prefix issue 

using defautldict makes key generation so keep in mind
"""


import collections
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we can make the dag
        # word len ^ 2 * len(longest word)
        
        keys = set() # fixed set of keys representing all the characters
        for word in words:
            for c in word:
                keys.add(c)

        # precompute defaults
        adj = {c : set() for c in keys}
        for i in range(0 , len(words)):
            if i + 1 < len(words):
                left, right = 0 , 0
                # try to find first different word
                while left < len(words[i]) and right < len(words[i + 1]):
                    if words[i][left] != words[i + 1][right]:
                        adj[words[i][left]].add(words[i + 1][right])
                        break
                    # equal keep moving
                    left += 1
                    right += 1

                if left < len(words[i]) and right == len(words[i + 1]):
                    return ""

        # we will iterate and use the topological sort 
        result , visited = [] , collections.defaultdict()

        def dfs(node):
            """
            Docstring for dfs
            
            :param node: node
            topological sort with cycle detection 
            [] is a repr of cycle detected
            # not in visited truly not visited
            # visited false, in path 
            # visited true marked as visited  
            """
            visited[node] = False # in path 

            ordering = []
            for nei in adj[node]:
                if nei not in visited:
                    sub_ordering = dfs(nei)
                    if not len(sub_ordering):
                        # cycle downstream 
                        return []
                    ordering.extend(sub_ordering)
                else:
                    if visited[nei] == False:
                        # direct nei is in path already 
                        return []    
        
            # marked as visited 
            visited[node] = True
            ordering.append(node)
            return ordering

    
        for key in keys:
            if key not in visited:
                subans = dfs(key)
                if len(subans) == 0:
                    # early break after cycle detected
                    # possible some other component was ok
                    result = []
                    break
                result.extend(subans)

        result.reverse()
        return "".join(result)