from typing import List

# rotated sorted array part 1

"""
1 2 3 4 5 , k = 0
5 | 1 2 3 4 ,   2 3 4 5 | 1 , k = 1 (left or right)
4 5 | 1 2 3 ,   3 4 5 | 1 2 , k= 2

inc | inc

if 3 then linear search or bring left closer 
ie;  left < mid > right linear search

if element > left 


                 mid
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104


left ..... mid ......right

"""

# shorter, optimized solution 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1

        while right - left + 1 > 3:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            

            if nums[left] < nums[mid]:
                # left partition 
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid

            else:
                # right partition 
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid



        for index in range(left , right + 1):
            if nums[index] == target:
                return index
        
        return -1



"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums[mid] >= nums[l] this case we add = so that ips of size <= 2
        # is given
        # otherwise we can also do something like [l , mid , r] and handle <=2
        # cases separately
        l, r = 0, len(nums) - 1
        required_index = -1

        while l <= r:
            mid = l + int((r - l) / 2)
            if nums[mid] == target:
                required_index = mid
                break
            elif nums[mid] >= nums[l]:
                # in the left side of the array
                if nums[l] <= target < nums[mid]:
                    # go in further to mock binary search
                    r = mid - 1
                else:
                    # in the other part, either target is smaller or greater than
                    # the input bounds
                    l = mid + 1
            else:
                # on the right side of the array
                if nums[mid] < target <= nums[r]:
                    # go in further, mock binary search
                    l = mid + 1
                else:
                    # in the other part lower than the lowest or greater
                    r = mid - 1

        return required_index
"""


# rotated sorted array part 2
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ans, l, r = False, 0, len(nums) - 1
        while l <= r:
            mid = l + int((r - l) / 2)
            # print("the split parts are as : ")
            # print(nums[l : mid + 1] , " : " , nums[mid + 1 : r + 1])
            if nums[mid] == target:
                ans = True
                break
            elif nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:
                # on the left side guaranteed
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # on the right side guaranteed
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return ans
"""
