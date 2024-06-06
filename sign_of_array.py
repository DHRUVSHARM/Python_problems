from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for element in nums:
            if element == 0:
                return 0
            elif element < 0:
                result = result ^ 1

        if result == 0:
            return -1
        else:
            return 1
