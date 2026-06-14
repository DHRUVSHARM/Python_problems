from typing import List

"""
problem approach

tree is rooted at node 1 
n nodes labelled from 1 to n 

given edges
need to construct parent array 

parent[1] = 1 # for simplicity 

precompute
dp[node][j] along with depth[node] simultaneously 

j can be depth atmost log (2 <= n <= 105)

find depth for each node and store 

for each query u , v: 
    if u == v return 0 

    find lca:
        find depth diff
        move deeper node , diff ancestor up 

    # once found lca
    dist (u , v) = depth(u) + depth(v) - depth(lca) 

    return 2**(dist - 1) % mod


TC : approx log(n) per query * query 


since we will have to use dfs, for building out the parent 
array we will calculate depth from there only 

"""

import collections
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        adj , depth = collections.defaultdict(list) , collections.defaultdict(int)
        depth[0] = 0
        n = len(edges) + 1 # number of nodes 
        # convert to 0 to n - 1

        for u , v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        parent = [None for _ in range(n)]
        parent[0] = 0
        max_depth = [0]

        def dfs(p , node):
            for nei in adj[node]:
                if nei != p:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    max_depth[0] = max(max_depth[0] , depth[nei])
                    dfs(node, nei)

        dfs(0 , 0)
        # print(parent)

        # at this point we have the parent and the depth correctly 

        depth_limit = 0
        while (1 << depth_limit) <= max_depth[0]:
            depth_limit += 1
        
        # print(depth_limit)

        # precompute dp[node][j]
        dp = [[None for _ in range(0 , depth_limit)] for _ in range(n)]

        for j in range(0 , depth_limit):
            for node in range(0 , n):
                if j == 0:
                    dp[node][j] = parent[node] # direct parent 
                else:
                    dp[node][j] = dp[dp[node][j - 1]][j - 1]
        

        # out of depth ancestors all loop back to 0 (1 converted root)

        def helper(node, k):
            # returns the kth ancestor of node 
            curr_node = node
            # print("k : " , k)
            j = 0
            while k:
                if k & 1 == 1:
                    # print("j : " , j)
                    curr_node = dp[curr_node][j] # jump to correct ancestor 
                j += 1
                k = k >> 1
            
            return curr_node


        res , MOD = [] , 10**9 + 7
        for u , v in queries:
            # print("query : " , u , " : " , v)
            if u == v:
                res.append(0)
            else:
                # shallow, deep
                deep = u - 1 if depth[u - 1] >= depth[v - 1] else v - 1
                shallow = u - 1 if depth[u - 1] < depth[v - 1] else v - 1 

                diff = depth[deep] - depth[shallow]
                # bring deep up 
                new_deep = helper(deep , diff)
                n_s = shallow 

                while new_deep != n_s:
                    new_deep = parent[new_deep]
                    n_s = parent[n_s]
                
                lca = n_s 
                # print("lca: ",  lca)

                dist = depth[deep] + depth[shallow] - 2*depth[lca]
                # print("dist : " , dist)
                # print("deep : " , depth[deep])
                # print("shallow : " , depth[shallow])
                # print("dist : " , dist)

                res.append((1 << (dist - 1)) % MOD)


        return res

