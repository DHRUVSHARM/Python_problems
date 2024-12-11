import collections
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result , elements = [] , collections.deque()
        for r in range(0 , k):
            while len(elements) and elements[-1][0] >= nums[r]:
                elements.pop()
            elements.append((nums[r] , r))
        
        # print(elements)

        if len(elements) == k and (elements[-1][0] - elements[0][0] + 1) == k:
            result.append(elements[-1][0])
        else:
            result.append(-1)
        
        left , r = 0 , k

        while r < len(nums):
            if elements[0][1] == left:
                elements.popleft()
            left += 1

            while len(elements) and elements[-1][0] >= nums[r]:
                elements.pop()
            elements.append((nums[r] , r))

            if len(elements) == k and (elements[-1][0] - elements[0][0] + 1) == k:
                result.append(elements[-1][0])
            else:
                result.append(-1)
            
            r += 1

        return result

"""
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result , elements = [] , collections.deque()
        for r in range(0 , k):
            while len(elements) and elements[-1][0] >= nums[r]:
                elements.pop()
            elements.append((nums[r] , r))
        
        print(elements)

        if len(elements) == k:
            result.append(elements[-1][0])
        else:
            result.append(-1)
        
        left , r = 0 , k

        while r < len(nums):
            if elements[0][1] == left:
                elements.popleft()
            left += 1

            while len(elements) and elements[-1][0] >= nums[r]:
                elements.pop()
            elements.append((nums[r] , r))

            if len(elements) == k:
                result.append(elements[-1][0])
            else:
                result.append(-1)
            
            r += 1

        return result
"""