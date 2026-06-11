# tree with n nodes 1 to n 
"""
n - 1 edges 
rooted at 1 

Select any one node x at the maximum depth. 
Return the number of ways to assign edge weights 
in the path from node 1 to x such that its total cost is odd.

from child              number of odd ways (even 2) + number of even ways (odd 1) = res
                        number of even ways = number of odd sum (odd) + number of even summ (even)


                        from leaf return  1 , 1

                        at any node odd count even count 

                        if only root 0



                        2^(max depth - 1)         
"""

from typing import List
import collections
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        adj = collections.defaultdict(list)
        m = 10**(9) + 7

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        root = 1 # known and it is a tree
        # atleast one edge will be there 

        
        def helper(par, node):
            max_depth = 0
            for nei in adj[node]:
                if nei != par:
                    # consider the edge and check max_depth 
                    max_depth = max(max_depth , 1 + helper(node, nei))
            
            return max_depth

        max_depth = helper(None , root)

        return 2**(max_depth - 1) % m