from typing import List

"""
nums is sorted in non-decreasing order.

-1               l           r                
    [0,  0,  1,  1,  1,  1,  2,  3,  3,  4]


"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left , k , curr_count = -1 , 0 , 0

        for r in range(0 , len(nums)):
            if r != 0 and nums[r] != nums[r-1]:
                # boundary 
                curr_count = 0
            
            # normal count case 
            curr_count += 1

            if curr_count > 2:
                pass
            else:
                left += 1
                nums[left] = nums[r]
                k += 1


        return k

