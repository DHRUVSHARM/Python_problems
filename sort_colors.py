from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in this algorithm we can use the DNF algo
        # since relative order does not matter and does not have to be preserved 

        left, right = -1 , len(nums)
        index = 0
        while index < right:
            if nums[index] == 0 and index > left:
                nums[left + 1] , nums[index] = nums[index] , nums[left + 1]
                left += 1
            elif nums[index] == 2:
                # we dont go into index >= r anyway 
                nums[right - 1] , nums[index] = nums[index] , nums[right - 1]
                right -= 1
            else:
                index += 1
        