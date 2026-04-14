from typing import List

"""
There are some robots and factories on the X-axis. 
You are given an integer array robot where robot[i] is the position of the ith robot. 
You are also given a 2D integer array factory where factory[j] = [positionj, limitj] 
indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.

dp[i][j] = min dist for robots ....i , ..j stations

 
        ""       0           4           6

""      0       inf          inf        inf

2       0       2    

2       0       

6       0

6       0


for i in robots:
    for j in stations:
        pass
        
dp[i][j] = min(

    dp[i][j - 1],
    abs(station[j] - robots[i]) + dp[i - 1][j - 1] # select robot move one station behind 
)

o(robot * factory * factory)
"""

import collections
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        temp_factory = []
        for element , limit in sorted(factory): # sorted by position already 
            temp_factory.extend([element] * limit)
        
        factory = temp_factory 

        dp = collections.defaultdict()
        dp[(-1 , -1)] = 0 # nothing required 

        # no factory base case 
        for i in range(0 , len(robot)):
            dp[(i , -1)] = float("inf")

        # no robot but factory base case 
        for j in range(0 , len(factory)):
            dp[(-1 , j)] = 0

        for i in range(0 , len(robot)):
            for j in range(0 , len(factory)):
                dp[(i , j)] = min(

                    dp[(i  , j - 1)], # do not use current factory 
                    dp[(i - 1 , j - 1)] + abs(robot[i] - factory[j])
                )
        
        # print(dp[(len(robot) - 1 , len(factory) - 1)])
        return dp[(len(robot) - 1 , len(factory) - 1)]