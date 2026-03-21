"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.




                5
    -1          -2          -5
-1

-1

dp[amt][i] = amt to make from 0 ... i
 =     for all j , max( dp[amt - coins[j]][i] + coins[j] , dp[amt][i-1] 

"""

from typing import List

import collections
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 2 solutions based on the dp method 
        dp = collections.defaultdict(int)
        coins.sort()

        for index in range(len(coins)):
            dp[(0 , index)] = 1

        for amt in range(1 , amount + 1):
            for index in range(len(coins)):
                if amt - coins[index] >= 0:
                    dp[(amt , index)] += dp.get((amt - coins[index] , index) , 0)
                dp[(amt , index)] += dp.get((amt , index - 1) , 0)   
                
        
        # print(dp)
        return dp[(amount , len(coins) - 1)]