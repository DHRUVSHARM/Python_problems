from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit , max_stock_price = max(0 , prices[-1] - prices[-2]) , max(prices[-1] , prices[-2])

        for index in range(len(prices) - 3 , -1 , -1):
            current_profit = max(
                max_stock_price - prices[index] , 0)
            max_profit = max(
                current_profit , 
                max_profit
            )
            max_stock_price = max(max_stock_price , prices[index])

        return max_profit
