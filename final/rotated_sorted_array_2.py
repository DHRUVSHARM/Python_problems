from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1

        if len(nums) == 0:
            return -1
        
        
        result = -1
        while left <= right:
            
            # handle 2 and 1 size case manually
            if (right - left + 1) <= 2:
                for index in range(left, right + 1):
                    if nums[index] == target:
                        result = index
                # break regardless
                break
                        
            
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                break

            else:
                # monotonic
                """
                if mid < l
                mid  + 1 ... r increase if target in there move right else left
                
                if mid > l
                l ... mid - 1 , check target if here then move left else right
                """

                if nums[mid] < nums[left]:
                    if nums[mid + 1] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                elif nums[mid] > nums[left]:
                    if nums[left] <= target <= nums[mid - 1]:
                        right = mid - 1
                    else:
                        left = mid + 1 
                else:
                    left += 1


        return True if result != -1 else False