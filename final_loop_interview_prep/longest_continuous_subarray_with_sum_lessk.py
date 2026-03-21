from typing import List

"""
notes 
this is a sliding window problem 
we need an effecient way to find the min and max element to solve the problem 
1 element is probably limti 0

 
       l   r
    [8,2,4,7]

    # also it will help, since we know that the max element in l .... r is actually 8
max    [7]


# need to understand, that the minimal element is never going to be 8 anymore , at leat   
min    [2 , 4 , 7]


at this point
l ... r
max elements , min elements are stored 

imp point 


r inc add stuff
move left to adjust, min 1, limit min 0
then add the length to consider for the global result 

"""
import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result , left , max_q , min_q = 0 , 0 , collections.deque() , collections.deque()

        for r in range(0 , len(nums)):
            # we want to keep >= 
            while len(max_q) and max_q[-1] < nums[r]:
                max_q.pop()
            # add the element 
            max_q.append(nums[r])

            # we want to keep <= for the min_q
            while len(min_q) and min_q[-1] > nums[r]:
                min_q.pop()
            # add the element 
            min_q.append(nums[r])


            # we tru to shif the left pointer to match constraints 
            # the way we are doing this we will always have one element even when left = right , the element itself should be there atleast 
            # and the limit at that poin is going to be zero , so we will end up there 
            while left <= r and (max_q[0] - min_q[0]) > limit:
                # shift left
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1

            result = max(result , r - left + 1)

        return result

