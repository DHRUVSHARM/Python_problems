"""

You are given a 0-indexed integer array nums and an integer p. 

Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.

Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 
basic problem 
pick a value which would be the max diff amongst all pairs
take the min of it 


1 1 2 3 7 10
 
 pick 3

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length

"""

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        # atleast one pair, and guaranteed that we can pair
        # ...FFFFFFTTTT...
        # problem  max diff of pairs <= value
        # always false -1 since abs diff so 0 min possible
        # always true will be abs(max - min)

        # atleast 2 since we checked the p 0 case beforehand 
        nums.sort()
        # print(nums)
        left, right = -1 , nums[-1] - nums[0]


        def helper(max_diff):
            # check if the max diff is possible (<= max diff, not exact)
            pair_count , index = 0 , 0
            
            while pair_count < p and (index + 1) < len(nums):
                if nums[index + 1] - nums[index] <= max_diff:
                    pair_count += 1
                    index += 2
                else:
                    # skip current 
                    index += 1

            return pair_count == p

        while left + 1 < right:
            mid = (right + left) // 2
         

            if helper(mid):
                # we can move to left 
                right = mid
            else:
                left = mid


        return right