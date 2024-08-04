from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans, ones_count = float("inf"), nums.count(1)
        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]

        for index in range(0, len(nums)):
            left, right = index, (index + (ones_count) - 1) % len(nums)
            if left == 0:
                # start
                ans = min(ans, ones_count - (nums[right] - 0))
            elif left > right:
                # circular
                ans = min(
                    ans, ones_count - ((nums[-1] - nums[left - 1]) + (nums[right]))
                )
            else:
                # normal
                ans = min(ans, ones_count - (nums[right] - nums[left - 1]))

        return ans
