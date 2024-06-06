from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        min_operations, sub_sum, left, target = float("inf"), 0, 0, sum(nums) - x
        # print("target : ", target)

        for r in range(0, len(nums)):

            sub_sum += nums[r]

            while left <= r and sub_sum > target:
                sub_sum -= nums[left]
                left += 1

            # print(left, " ", r, sub_sum)
            if sub_sum == target:
                # print("consider : ", left, " ", r)
                min_operations = min(min_operations, len(nums) - (r - left + 1))

        return -1 if min_operations == float("inf") else min_operations
