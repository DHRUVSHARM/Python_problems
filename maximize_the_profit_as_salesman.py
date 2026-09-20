from typing import List


"""

selections for overlapping are not allowed 


[0,0,1],[0,2,2],[1,3,2]]

(1)
00

(2)
0-------2
    
    (2)
    1---------3



    
# for the first element just select it 

sort by end time and pick the first end < start

< >= bl

bl(start) - 1 # strict less

<= > br

dp[i] = max(
    dp[i - 1],
    goldi + dp[rho]

)

"""

from bisect import bisect_left
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        n = len(offers)
        dp = [float("-inf ") for _ in range(0 , n)]
        offers.sort(key = lambda e : (e[1] , e[0])) # sort by the end time 

        dp[0] = offers[0][2] # always select all houses 

        for index in range(1 , n):
            dp[index] = dp[index - 1]
            idx = bisect_left(offers , offers[index][0] , 0 , index, key=lambda e : e[1]) - 1 
            dp[index] = max(
                dp[index],
                (0 if idx == -1 else dp[idx]) + offers[index][2]
            )

        return dp[n - 1]