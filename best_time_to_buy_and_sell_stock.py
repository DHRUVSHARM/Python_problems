"""
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


to choose a single day to buy a stocke
and then another to sell the stock 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        result = 0  # cannot sell initially 

        for sell_index in range(1 , len(prices)):
            result = max(result , max(0 , prices[sell_index] - min_buy))
            min_buy = min(min_buy , prices[sell_index])
        
        return result