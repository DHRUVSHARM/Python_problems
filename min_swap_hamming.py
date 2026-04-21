from typing import List
import collections
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        adj = collections.defaultdict(set) # prevent duplicate edges 

        for u , v in allowedSwaps:
            adj[u].add(v)
            adj[v].add(u)
        

        freq_target = collections.defaultdict(int) # target dfs freq
        indices_collected = set()

        visited = set()
        def dfs(node):
            visited.add(node)
            freq_target[target[node]] += 1
            indices_collected.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    subans = dfs(nei)
            
        
        result = 0
        for index in range(0 , len(source)):
            if index not in visited:
                freq_target = collections.defaultdict(int) # target dfs freq
                indices_collected = set()
                dfs(index)

                diff = 0
                for index in indices_collected:
                    if freq_target[source[index]] == 0:
                        diff += 1
                    else:
                        freq_target[source[index]] -= 1
                result += diff

        return result