import collections
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # first we need to build a graph to represent the tree
        adj = collections.defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        # we will do bottom up dp where return type is (sum , partitions)
        def helper(node):
            visited.add(node)
            # we will atleast add this
            tree_sum , tree_partitions = values[node] , 1
            for v in adj[node]:
                if v not in visited:
                    sum , partitions = helper(v)
                    tree_sum += sum
                    if sum % k == 0:
                        tree_partitions += partitions
                    else:
                        tree_partitions += (partitions - 1)
            
            # print(node , " : " , tree_partitions)
            return tree_sum , tree_partitions

        sum , ans = helper(0)
        return ans