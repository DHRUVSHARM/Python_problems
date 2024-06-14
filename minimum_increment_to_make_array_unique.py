from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        seen, ans = set(), 0
        max_in_set = float("inf")

        for element in nums:
            if element not in seen:
                # element in the future that will become the next frontier
                max_in_set = element  # can guarantee this
            else:
                # we need to change this element, what it becomes will be the next frontier
                max_in_set += 1
                ans += max_in_set - element
            seen.add(max_in_set)

        return ans
