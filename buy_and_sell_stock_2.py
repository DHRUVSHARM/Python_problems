from typing import List

"""

[7,1,5,3,6,4]
s = [6 , 4]


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # dp[i] : max profit from i... onwards
        dp = [0 for _ in range(len(prices))]
        s = [(prices[-1] , len(prices) - 1)]

        for index in range(len(prices) - 2 , -1 , -1):
            # we need to maintain the value greater than in the increasing stack 
            # print(s)
            while s and prices[index] >= s[-1][0]:
                # we can pop the equal values as well since they will not yield profit anyway
                s.pop()
            
            dp[index] = dp[index + 1]
            if len(s):
                # we have a closest next value 
                # can consider this greedily and consider from that point again
                dp[index] = max(
                    dp[index] , # not consider
                    (s[-1][0] - prices[index]) + dp[s[-1][1]] # consider closest increasing and optimal from that point after
                )
            
            # push this in the stack 
            s.append((prices[index] , index))
            # print(s)
            # print("--------------------------------------------")

        return dp[0]