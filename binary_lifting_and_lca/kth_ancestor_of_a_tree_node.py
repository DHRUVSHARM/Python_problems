from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n # number of nodes ( 0 to n - 1 ) 
        self.parent = parent # parent[i] : parent of i
        self.depth = {} # depth of node
        
        LIMIT =  5 * 10**4
        j = 0
        while (1 << j) <= LIMIT:
            j += 1

        # find the power that will cover the tree in worst unbalanced case 
        limit = j


        # precompute dp 
        self.depth[0] = 0
        self.parent[0] = 0 # loopback from root instead of -1 

        dp = [[None for _ in range(0 , limit)] for _ in range(0 , n)]
        for j in range(0 , limit):
            # print("j : " , j)
            for node in range(0 , n):
                if j == 0:
                    dp[node][j] = parent[node]
                    if node not in self.depth and parent[node] in self.depth:
                        self.depth[node] = self.depth[parent[node]] + (1 << j)
                else:
                    anc = dp[node][j - 1]
                    dp[node][j] = dp[anc][j - 1]
                    if node not in self.depth and anc in self.depth:
                        self.depth[node] = self.depth[anc] + (1 << (j - 1))
            # print(self.depth , " currently ")
        
        self.dp = dp
        # print(self.depth)


    def getKthAncestor(self, node: int, k: int) -> int:
        # if k is greater than the max depth of the node then we will return -1 
        # idea is to answer these queries in log n time 
        # print(node)
        # print(self.depth)
        # if node not in self.depth:
            # print("not found in depth ")
        
        if k > self.depth[node]:
            return -1
        
        j , curr_node = 0 , node 
        while k != 0:
            if (k & 1) == 1:
                # set bit 
                curr_node = self.dp[curr_node][j]
            j += 1
            # move the bit used to the right to sink
            k = k >> 1
            # print(curr_node)

        return curr_node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)