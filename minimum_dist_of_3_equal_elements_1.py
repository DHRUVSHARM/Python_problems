from typing import List
"""
A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].


i   j   k

(i - j) + (j - k) + (k - i) = i

return min dist of good tuple 

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.


0  1 2 3 4
[1,2,1,1,3]


1 : 0 , 2
2 : 1



"""

import collections
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = float("inf")
        element_map = collections.defaultdict(collections.deque)

        for index, element in enumerate(nums):
            element_map[element].append(index)
            if len(element_map[element]) == 3:
                # can consider 
                result = min(
                    result,
                    2 * (element_map[element][-1] - element_map[element][0])
                )
                element_map[element].popleft()
        
        return -1 if result == float("inf") else result