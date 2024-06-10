from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = [element for element in heights]
        sorted_heights.sort()

        ans = 0
        for curr, actual in zip(heights, sorted_heights):
            ans += 1 if curr != actual else 0

        return ans
