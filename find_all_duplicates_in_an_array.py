from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # we will use the fact that all nums are in between 1 to n and indices
        # range from 0 to n - 1

        ans = []

        for index, value in enumerate(nums):
            value = abs(value)
            if nums[value - 1] > 0:
                # we see this number for the first time
                nums[value - 1] *= -1
            else:
                # number seen for second time
                ans.append(value)

        return ans
