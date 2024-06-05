from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # delta = changed - original
        ans = sum(nums)
        delta = [(nums[index] ^ k) - nums[index] for index in range(len(nums))]
        delta.sort(reverse=True)
        index = 1
        while index < len(nums):
            if delta[index] + delta[index - 1] > 0:
                ans += delta[index] + delta[index - 1]
            else:
                break
            index += 2

        return ans
