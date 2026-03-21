"""
Docstring for buy_and_sell_stock_transaction_fee
we will try to work on this to solve iteratively 

prices = [1,    3,      2,      8,      4,      9],     fee = 2
          buy                   sell                     
                                buy  
assume that we
can buy after selling on the same day

dp(buy , index) = max( -p[index] + dp[sell][index + 1] , dp[buy][index + 1] )
dp(sell, index) = max( +p[index] - transaction fee + dp[buy][index] , dp[sell][index + 1] )

# iteratively
dp 

"""

from typing import List
import collections

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
       
        # buy : 0
        # sell : 0

        dp = collections.defaultdict()

        """
        dp(buy , index) = max( -p[index] + dp[sell][index + 1] , dp[buy][index + 1] )
        dp(sell, index) = max( +p[index] - transaction fee + dp[buy][index] , dp[sell][index + 1] )
        """

        dp[(0 , len(prices))] = 0
        dp[(1 , len(prices))] = 0

        for index in range(len(prices) - 1 , -1 , -1):
            dp[(0 , index)] = dp.get((0 , index + 1) , 0)
            dp[(1 , index)] = dp.get((1 , index + 1) , 0)

            dp[(0 , index)] = max(
                dp[(0 , index)] , -1 * prices[index] + dp[(1 , index + 1)]
            )

            dp[(1 , index)] = max(
                dp[(1 ,index)] , prices[index] - fee + dp[(0 , index)]
            )


        return dp[(0 , 0)]