from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        maximal_score, left, right, minimal, width = nums[k], k, k, nums[k], 1

        while left - 1 >= 0 or right + 1 < len(nums):
            # one or both conditions true

            if left - 1 >= 0 and right + 1 < len(nums):
                # both conditions are true
                if nums[left - 1] > nums[right + 1]:
                    minimal = min(minimal, nums[left - 1])
                    left -= 1
                else:
                    minimal = min(minimal, nums[right + 1])
                    right += 1
            else:
                # one condition is true
                if left - 1 >= 0:
                    # left is true, right isn't
                    minimal = min(minimal, nums[left - 1])
                    left -= 1
                else:
                    # right is true, left isn't
                    minimal = min(minimal, nums[right + 1])
                    right += 1

            width += 1
            maximal_score = max(maximal_score, minimal * (width))

        return maximal_score
