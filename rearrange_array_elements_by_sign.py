from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index, negative_index, result = 0, 1, [0 for _ in range(0, len(nums))]

        for element in nums:
            if element >= 0:
                result[positive_index] = element
                positive_index += 2
            else:
                result[negative_index] = element
                negative_index += 2

        return result
