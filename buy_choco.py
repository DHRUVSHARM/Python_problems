from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        first_l, second_l = (prices[1], prices[0]) if prices[0] <= prices[1] else (prices[0], prices[1])
        ans, min_sum = money, first_l + second_l

        if money - min_sum >= 0:
            ans = money - min_sum

        for i in range(2, len(prices)):
            if prices[i] <= second_l:
                first_l, second_l = second_l, prices[i]
            elif second_l < prices[i] <= first_l:
                first_l = prices[i]
            else:
                # not include it
                pass

            min_sum = min(
                min_sum,
                first_l + second_l
            )

        if money - min_sum >= 0:
            ans = money - min_sum

        return ans
