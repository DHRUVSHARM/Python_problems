from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) - 1
        result = float("inf")

        while right - left + 1 >= 3:
            mid = (left + right) // 2
            result = min(result , nums[mid])
            
            if nums[mid] > nums[0]:
                # strictly greater condition indicating left side
                # 0 1 2 ... 3 3 5 so on 
                # print("left")
                if nums[mid - 1] <= nums[mid]:
                    # check increase or equal
                    if nums[0] >= nums[-1]:
                        # find if drop on right if found here move right
                        left = mid
                    else:
                        # no drop move left
                        #print("right move")    
                        right = mid
                else:
                    # already at drop move right, we wont come here probably 
                    left = mid
            elif nums[mid] == nums[left]:
                # nums[mid] <= nums[0] and also equal to left, can have or equal or dip then come back to sames
                # as on the left so move one ahead to check  
                left += 1
            else:
                # in right side always better to move right towards min
                right = mid

        for index in range(left, right + 1):
            result = min(result, nums[index])

        return result
        