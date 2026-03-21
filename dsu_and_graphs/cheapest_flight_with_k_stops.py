from typing import List

"""
There are n cities connected by some number of flights. 

You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


k stops -> k + 1 edges
note the word atmost

something of cost that is minimal, might take more stops 
this is an issue, we are ready to sacrifice cost for k constraint 

src : 0 dst 3 

go over edges 




    0       1       2       3       4       5

0   0       100     500     inf     inf     inf 

1   0       100     200     


"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # base case no stops 
        dp = [float("inf") for _ in range(0 , n)]
        dp[src] = 0 # with 0 edges only the src is reachable 

        for edge_limit in range(1 , k + 2):
            temp = [float("inf") for _ in range(0 , n)]
            # dp[v][k] = min(dp[v][k-1] , u - v + dp[u][k - 1])
            # print("prev dp : " , dp)
            for u, v, w in flights:
                # print("u , v , temp[v] : " , u , " : " , v , " : " , w , " dp[v] " , dp[v] , " : ",  dp[u] + w)
                temp[v] = min(temp[v] , dp[v] , dp[u] + w)
        
            dp = temp
            # print(dp)
        
        return -1 if dp[dst] == float("inf") else dp[dst]



