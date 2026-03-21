from typing import List
"""

we will use the atmost k - atmost k - 1 for this solution the other approach will only 
be discussed

if we try to get the exact goal we will have an issue, 
using r to count the number of subarrays ending at r is not possible, 
so we try to count per l .. r point, 

2 + 2

till fail increase then move left, count while moving  

the fact that we have a one and removing than will cross the boundary and therefore we will have the earlies 9 
for the next window makes the sliding window method work



1 + 1 - 1   



3 pointer method

move r till we reach the goal
basically add stuff and count ones

if we find the goal then 
    make p = l
    a while loop to move l till invalid
    then add the l - p
    will give the answer with r 

                3                           10
                p                           l   r                                                                                     
    1   0   1   0   0   0   0   0   0   1   0   1

                                      
        p       l                               r                                                                                     
    1   0   1   0   0   0   0   0   0   1   0   1

    p   l  r
    0 1 0 1 0 
1 + 2 + 3 + 4 fo   r simple 0 values 
1 + 2 + 3 + 4 +5
     p               r l
    [0,  0,  0,  0,  0]


    atmost solution 

    keep moving r and adding till we exceed the goal 
    
    if exceed
        we try to creep in while the condition is valid again 
        once valid consider  

        goal = 1
      l r
    1 1 1 1

        l           r
    1   0   1   0   1


"""


class Solution:

    def helper(self, arr , k):
        """
        returns the number of subarrays with sum atmost k 
        """
        result , left , curr_sum = 0 , 0 , 0
        for r in range(0 , len(arr)):
            curr_sum += arr[r]
            
            # exceeded
            while left <= r and curr_sum > k:
                curr_sum -= arr[left]
                left += 1
            result += (r - left + 1)

        return result

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.helper(nums , goal) - self.helper(nums , goal - 1)