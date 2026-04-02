from typing import List

"""
There is a directed graph of n colored nodes and m edges. 

The nodes are numbered from 0 to n - 1.

n node, each colored (0 , n - 1)

You are given a string colors where colors[i] 

is a lowercase English letter representing the color of the 

ith node in this graph (0-indexed). 

You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk 

such that there is a directed edge from xi to xi+1 for every 1 <= i < k. 

The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.


algo 

topological sort dfs, based to detect cycle
we have n nodes 0 - n - 1

dp[node][c] = max path explored from node of color c
    for all outgoing max(dp[nei][c]) + 1 if color of curr is c else 0 

    
for a node 
for all nei:
    for all c in 1 , 26
        dp[node][c] = max(dp[node][c]  , dp[nei][c])

dp[node][c] += 1 (add curr to max path collected)

across all edges, 26 times so 26m
we will cache the results for an index once visited useful for final check as well

"""
import collections
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dp = [[0 for _ in range(0 , 26)] for _ in range(n)] # dp[n][26]
        adj , visited = collections.defaultdict(list) , {}


        for u , v in edges:
            adj[u].append(v) # directed edge

        # with topo does not matter which node we start 
        def dfs(node):
            # at this point we are at a node which has not been recorded or visited 
            visited[node] = False # simple entry 
            visited[node] = True
            color = ord(colors[node]) - ord('a') # store color 

            for nei in adj[node]:
                if nei in visited and visited[nei] == True:
                    # cycle
                    return True
                
                if nei not in visited:
                    # need to calculate 
                    has_cycle = dfs(nei)
                    if has_cycle == True:
                        return True # no checking, we encountered cycle 
                else:
                    # already calculated in visited and we checked it was not true
                    # we will not visit again 
                    pass
                
                # at this point we have stored the req data for nei either already or via call
                for c in range(0 , 26):
                    dp[node][c] = max(dp[node][c] , dp[nei][c])
            
            # add the current color to the max collected 
            dp[node][color] += 1
            visited[node] = False
            return False # no cycle
        
        for node in range(0 , n):
            if node not in visited:
                has_cycle = dfs(node)
                if has_cycle:
                    return -1
        
        result = 0
        for node in range(0 , n):
            for c in range(0 , 26):
                result = max(result, dp[node][c])
        
        return result

        
