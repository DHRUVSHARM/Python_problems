from typing import List

"""
n == colors.length
2 <= n <= 100
0 <= colors[i] <= 100
Test data are generated such that at least two houses have different colors.
                 l     r
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.


l                                                        r
[1, 1,  1,  1 , 1 , 1 , 6,  1 6 6 6 6 6 6 6 6    1,  1,  1]


r - l + (off)

"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left , dpl ,  right , dpr , result = 0 , 0 , len(colors) - 1 , 0 , 0
        prev_left , prev_right = colors[left] , colors[right]

        while left <=  right:
            if colors[left] == colors[right] and prev_left == colors[left] and prev_right == colors[right]:       
                dpl += 1
                prev_left, prev_right = colors[left] , colors[right]
                left += 1
                right -= 1
            else:
                # print(left,  ":" , right)
                result = max(result , abs(left - right) + dpl)
                while left < right and colors[left] != colors[right]:
                    left += 1
                dpl = 0
                prev_left, prev_right = colors[left] , colors[right]
    
        
        return result
