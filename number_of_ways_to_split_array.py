from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans , total , curr = 0 , sum(nums) , 0

        for index in range(0 , len(nums) -1):
            curr += nums[index]
            if curr >= (total - curr):
                ans += 1 

        return ans