from typing import List
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # convert the points on the square to 1d

        new_points = []

        for x , y in points:
            if x == 0:
                new_points.append(abs(y))
            elif y == side:
                new_points.append(side + abs(x))
            elif x == side:
                new_points.append(2*side + abs(side - y))
            else:
                new_points.append(3*side + abs(side - x))

        # we have the points in sorted order on 1d line at this point 
        # need to sort the transformed input since the input may not be sorted 
        # points were unique so transformation will be unique as well
        new_points.sort()
        # print(new_points)
        
        # we need to find the max min dist between k points
        # TTTTTTFFFFFF
        # >= x therfore >= x - 1 is also valid 

        perimeter = 4*side
        # 0 .....  start    ,,,,,,,     query point ......perimeter
        # p - end + start - 0 >= limit
        # p - limit + start >= end
        # end <= p - limit + start , if end > p - limit + start , -> invalid point 

        """
        bisect_left means:
        first index where arr[i] >= target

        < target  >= target
        FFFFFFFFFFFF  TTTTTTTTTTTT
        
        T value for bisect left 
        idx - 1 for last one strictly less 

        we can use bisect left from start, to find the first >= start + limit
        and at the same time check if end <= p - limit + start, if not then invalid 
        
        All points[i] are unique.
        4 <= k <= min(25, points.length
        """

        # print(new_points)

        def helper(min_dist):
            # find if we can select k points with min distance >= min_dist
            # we will need to check all the possible start points for considering 
            n = len(new_points)
            for start_index in range(0 , n):
                start = new_points[start_index]
                curr_point = new_points[start_index]
                points = 1 # current point 

                while points < k:
                    new_point_index = bisect_left(new_points , curr_point + min_dist) # find first index that is min_dist away from curr point 
                    if new_point_index == n:
                        break
                    
                    # ensure not in forbidden wrap around region wrt current start 
                    if new_points[new_point_index] > perimeter - min_dist + start:
                        break

                    # can take this point 
                    points += 1
                    curr_point = new_points[new_point_index]
                
                if points == k:
                    return True

            return False

        left = 0 
        # right = max(new_points[-1] - new_points[0] , perimeter - (new_points[-1] - new_points[0])) + 1
        right = side + 1
        # print(right)
        # T : since points are distinct, F: max dist + 1
        """
        another logic for the bound is as follows, we 
        the max min dist between 2 points, on the sq boundaries if we have to choose 4 points, 
        this will be the min betwen any 2, and that can be atmost side, bevause after they will be pushed to one 
        edge making the distancew as <= side so side + 1 is also a bound 
        """

        while left + 1 < right:
            mid = (left + right) // 2

            if helper(mid):
                left = mid
            else:
                right = mid

        return left

