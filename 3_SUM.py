# Problem summary:
# - Find all unique triplets in nums whose values sum to 0.
#
# Approach:
# - Sort nums so duplicates are adjacent and two-pointer movement is possible.
# - Fix one value as the frontier, then search the remaining suffix for two
#   values whose sum is the negative of that frontier.
# - Move the left/right pointers inward based on whether their sum is too small
#   or too large, and skip repeated values after each move to avoid duplicate
#   triplets.
# - After each frontier value, skip all duplicates of that fixed value.
#
# Pattern:
# - Sorting plus two pointers, reducing 3Sum to repeated 2Sum scans.
#
# Complexity:
# - Time: O(n^2), where n is the length of nums.
# - Space: O(1) extra space besides the output list.
#
# Example dry run:
# - Input: nums = [-1, 0, 1, 2, -1, -4]
# - Sort: nums becomes [-4, -1, -1, 0, 1, 2].
# - Frontier -4: target is 4; left/right pairs never reach 4, so no triplet.
# - Frontier -1: target is 1; left=-1 and right=2 sum to 1, so add
#   [-1, -1, 2], then skip duplicate pointer values.
# - Continue frontier -1 scan: left=0 and right=1 sum to 1, so add
#   [-1, 0, 1].
# - Skip duplicate frontier -1, then later frontier values find no new triplets.
# - Output: [[-1, -1, 2], [-1, 0, 1]].

from typing import List

if __name__ == "__main__":
    for i in range(0, 0):
        print("in loop !!!")


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # print(nums)

        def twoSum(first_element, l, r):
            target = -1 * first_element
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([frontier, nums[l], nums[r]])
                    left_element = nums[l]
                    while l < len(nums) and nums[l] == left_element:
                        l += 1

                    right_element = nums[r]
                    while r >= 0 and nums[r] == right_element:
                        r -= 1

                elif nums[l] + nums[r] < target:
                    left_element = nums[l]
                    while l < len(nums) and nums[l] == left_element:
                        l += 1
                else:
                    right_element = nums[r]
                    while r >= 0 and nums[r] == right_element:
                        r -= 1

        i = 0
        while i < len(nums) - 2:
            frontier = nums[i]
            twoSum(frontier, i + 1, len(nums) - 1)
            while i < len(nums) and nums[i] == frontier:
                i += 1

        return result
