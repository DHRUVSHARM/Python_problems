from typing import List

"""
                              
Input: points = [[1,1],[2,2],[3,3]]

quadratic * constant 
slope -> point set mapping

# dispersed view of points
(2 - 1) / (2- 1) -< slope 



Output: 3

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

[[0,0] , [4,5], [7,8], [8,9], [5,6], [3,4], [1,1]]

defaultdict(<class 'set'>, 
{(5, 4): {(1, 1), (4, 5), (5, 6), (0, 0)}, 
(8, 7): {(1, 1), (8, 9), (7, 8), (0, 0)}, 
(9, 8): {(8, 9), (0, 0)}, 
(6, 5): {(5, 6), (0, 0)}, 
(4, 3): {(1, 1), (4, 5), (3, 4), (0, 0)}, 

(1, 1): {(3, 4), (0, 0), (1, 1), (4, 5), (8, 9), (5, 6), (7, 8)}, 

(7, 6): {(1, 1), (7, 8)}, 

(3, 2): {(1, 1), (3, 4)}})

y = mx + c


slope = 
y - mx = c


# pick a point, 
# pick next point, calcualte slope, and note it down , then increment as you see more points, 
# a , b         bc      ca
# slope: 2
# next point reset
# a . b         dd      dd          fff
# slope y2 - y1 , x2 - x1
# 1 , 2 3, 2 # same horizontal line : dx = 0
# same vertical line : dy = 0
# (-1 , 2 ) ,  (1 , -2) # move the sign to the numerator 

point               x           
"""
import collections
import math

class Solution:
    
    def helper(self, src, dest):
        numerator , denominator = (dest[1] - src[1]) , (dest[0] - src[0])
        # print("here : " , numerator, ":" , denominator)
        if denominator == 0 or numerator == 0:
            # no 0, 0 since coincident points not in input 
            if denominator < 0:
                denominator *= -1
            if numerator < 0:
                numerator *= -1
        else:
            # both are not zero 
            if denominator < 0:
                # move sign to numerator 
                denominator *= -1
                numerator *= -1
        
        gcd = math.gcd(numerator , denominator)
        numerator //= gcd
        denominator //= gcd

        return (numerator , denominator)
         


    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 2 # min ans

        for start in range(0 , len(points)):
            slopes = collections.defaultdict()
            # print("start : " , points[start])
            for point in range(start + 1 , len(points)):
                s , p = points[start] , points[point]
                normalized_slope = self.helper(s , p)
                # print("normalized : " , normalized_slope)
                if normalized_slope not in slopes:
                    slopes[normalized_slope] = 2 # 2 points
                else:
                    slopes[normalized_slope] += 1 # add the point
                # print(slopes) 
                ans = max(ans , slopes[normalized_slope])
        

        return ans