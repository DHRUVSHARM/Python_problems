from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, left, occur, subans, target = len(nums), 0, 0, 0, max(nums)

        for r in range(0, n):
            if nums[r] == target:
                occur += 1

            if occur <= k - 1:
                subans += r - left + 1
            else:
                while left <= r and occur > k - 1:
                    if nums[left] == target:
                        occur -= 1
                    left += 1
                subans += r - left + 1

        return ((n * (n + 1)) // 2) - subans
