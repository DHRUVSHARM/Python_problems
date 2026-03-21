from typing import List

"""

Example 1:

                           l   r
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 result = [3 , 3 , 5 , 5 , 6 , 7]

 
# think this should be fine ? 
[7]

keep the index, element together , and pop out if not in current range > 

first move left and pop if it is same as the beginning, else let it be 
then add in right pop out irrelevant stuff for the current window
append the answer at the beginning of the array 

equal elements add them >= deque

 """

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result , q = [] , collections.deque()

        for index in range(0 , k):
            while len(q) and q[-1] < nums[index]:
                q.pop()
            # add the element >= order
            q.append(nums[index])
        
        # record the first answer 
        result.append(q[0])

        left = 0
        for right in range(k , len(nums)):
            # push left
            if len(q) and q[0] == nums[left]:
                q.popleft()
            left += 1

            # consider right
            while len(q) and q[-1] < nums[right]:
                q.pop()
            q.append(nums[right])

            # add result
            # guaranteed to have atleast one element 
            result.append(q[0])


        return result