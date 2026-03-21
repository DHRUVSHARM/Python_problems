from typing import List

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

pick the smaller from left and right 
consider it , sincer it will be the maximal width possible 


l                 r
[1,8,6,2,5,4,8,3,7]

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0 , len(height) - 1 , 0

        while left < right:
            result = max(
                result, 
                min(height[left] , height[right]) * (right - left)
            )

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return result