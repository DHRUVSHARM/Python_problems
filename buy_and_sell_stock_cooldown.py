"""
Docstring for buy_and_sell_stock_cooldown

max profit 

can complete as many transactions 

buy -> sell -> cooldown 

[   1,  2,  3,  0,  2]
buy val  
sell    s

     (sell, i + 1)
-1 + [2,3,0,2]
  

if i + 1 out of bound -float("inf")

-flot("inf) 9

(buy, i) -> max([-stock[i] + [(sell , i + 1)] , buy(i + 1))
(sell, i) -> max( +stock[i] + (buy , i + 2) , sell(i + 1))


caching 2 * len(stock span)
"""


from typing import List
import collections

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at least one price length
        dp = collections.defaultdict()

        """
        (buy, i) -> max([-stock[i] + [(sell , i + 1)] , buy(i + 1))
        (sell, i) -> max( +stock[i] + (buy , i + 2) , sell(i + 1))
        """

        def dfs(state , index):
            if index >= len(prices):
                # if state == 0:
                return 0
                # else:
                    # not selling is unprofitable
                    # return float("-inf")
            
            if (state, index) in dp:
                return dp[(state , index)]

            ans = float("-inf")
            if state == 0:
                # buy 
                ans = max(
                    ans ,
                    -1 * prices[index] + dfs(state ^ 1 , index + 1) ,
                    dfs(state , index + 1)
                )
            else:
                # sell
                ans = max(
                        ans ,
                        prices[index] + dfs(state ^ 1 , index + 2) ,
                        dfs(state , index + 1)
                    )
            
            dp[(state , index)] = ans
            return dp[(state , index)]


        # we will get 0 if answer is negative 
        return max( dfs(0 , 0) , 0)


