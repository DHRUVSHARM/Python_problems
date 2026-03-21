
"""
0


target

l       mid        r
      m-1  mid


0      3       6
[4,5,6,7,0,1,2]
l             r

mid > mid + 1
mid < mid - 1
l ... mid - 1 mid ... 1



  m
l   r

l   r
[1 , 2]

     l
-inf [2 , 1] +inf

-inf [1 , 2 ,3 ,4 ,5] +inf


     mid
[1 , 2 , 3 , 4]

    mid
3   4  1  2


l  m  r      
1 2 3 4


  l           m                      r                       
 7   8   9   10  1   2   3   4   5   6  

 if   mid - 1   mid    mid + 1

 
if mid
    return 

elif mid - 1  < mid < mid + 1


    if mid < l
    mid  + 1 ... r increase if target in there move right else left
    
    if mid > l
    l ... mid - 1 , check target if here then move left else right

else:
    found pivot
    mid < mid - 1
        [l ... mid - 1] , [mid + 1 ... r]

    or

    mid > mid + 1
    [l ... mid - 1] , [mid + 1 ... r]
    simple check 




 check if mid < l if yes,  left has l > stuff , move left  if target > l , right if mid + 1 < target < r
 check if mid  

"""

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

            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
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
                else:
                    if nums[left] <= target <= nums[mid - 1]:
                        right = mid - 1
                    else:
                        left = mid + 1 
            else:
                # found pivot 
                pass
                """
                found pivot
                mid < mid - 1
                    [l ... mid - 1] , [mid + 1 ... r]

                or

                mid > mid + 1
                [l ... mid - 1] , [mid + 1 ... r]
                simple check 
                """

                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                elif nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    # cannot find anywhere
                    break


        return result
            



