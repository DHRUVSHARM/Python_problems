from typing import List
# [2,7,11,15]
# l  ,,,,,  r
# 17

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0 , len(nums) - 1
        nums_indices = [(element, index) for index, element in enumerate(nums)]
        nums_indices.sort()

        while left < right:
            if nums_indices[left][0] + nums_indices[right][0] == target:
                break
            elif nums_indices[left][0] + nums_indices[right][0] < target:
                left += 1
            else:
                right -= 1

        # one answer exists 
        return [nums_indices[left][1] , nums_indices[right][1]]