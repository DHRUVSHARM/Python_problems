"""
Docstring for backtracking.next_permutation
# none greater  ?
 ind j
1 4         7 4 4 3 2 1

1 7         1 2 3 4 4 4




    ind   j 
1 4 5   8 7 3 2 1
    
    ind   j
1 4 7   8 5 3 2 1

147 81235

145 87321
147 12358

"""

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index = len(nums) - 2
        #          pivot
        # ..... index < | index + 1 >= > > ....
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        
        if index < 0 :
            # descending order , swap 
            pass
        else:
            #     ind
            # 1 4 5     8 7 5 3 2 1

            # atleast the next to 5 will be enough to swap 
            # but we try to find the least element that is 
            # greater , equal will not work and will infact create an equal element as the next perm 
            j = len(nums) - 1
            while j > index and nums[j] <= nums[index]:
                j -= 1
            
            # print(nums[index] , " : " , nums[j])
            # found the swap 
            #     ind        j 
            # 1 4 7    9 9 8 5 5 3 2 1
            
            nums[index] , nums[j] = nums[j] , nums[index]

        # swap index + 1 :  in place
        left , right = index + 1 , len(nums) - 1
        while left < right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
        
        return nums