from typing import List

"""
Example 1:
                 i   j
Input: values = [8,1,5,2,6]
Output: 11



Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i , res = values[0] + 0 , -1 

        for j in range(1 , len(values)):
            res = max(res , max_i + values[j] - j)
            max_i = max(max_i , values[j] + j) # store for next j 
    
        return res
        
