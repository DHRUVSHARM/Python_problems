
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



"""
1 -> 2 
4 <- 3

1: [2 , 3 , 4]

  <-
1 -> 2
    -> 3
    -> 4

otherwise clone and call on the neighbours
1 -> [2 , 3 , 4]

# if cloned, visited make connection 
2 -> [1]

3->[1]
4 -> 1
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import collections
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = collections.defaultdict()


        def dfs(node):
            if not node:
                return node
            clone_node = None
            if node not in mapping:
                # make the clone 
                clone_node = Node(node.val)
                mapping[node] = clone_node
            else:
                clone_node = mapping[node]
                return clone_node

            if node.neighbors:
                # we have children
                for child in node.neighbors:
                    cloned_child = dfs(child)
                    clone_node.neighbors.append(cloned_child)
            
            return clone_node

        return dfs(node)