from typing import List

"""

1   2   3   4   5   


sort by the end time 
we can then select end <= start = rho

< >=
<= > br(start) - 1

dp[i] = max(
    dp[i - 1],
    dp[rho] + (end - start) * tip # can overlap
)


"""
from bisect import bisect_right
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda element : (element[1] , element[0])) 
        # does not matter, anyways we are always considering the skip

        # print(rides)

        n = len(rides)
        dp = [float("-inf") for _ in range(n)]

        dp[0] = (rides[0][1] - rides[0][0]) + rides[0][2] # always better to pick up the passenger 

        for i in range(1 , n):
            dp[i] = dp[i - 1]
            idx = bisect_right(rides, rides[i][0] , 0 , i , key=lambda element : element[1]) - 1 # check by end 
            # print("idx : " , idx)
            dp[i] = max(
                dp[i],
                ((0 if idx == -1 else dp[idx]) + (rides[i][1] - rides[i][0]) + rides[i][2])
            )

        # print(dp)
        return dp[n - 1]
