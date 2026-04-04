"""
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.

ex : 

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
Thus, the answer is 3.

           |2|
            2              |5|            |7|             10
            1                                              7 

            2  + 1


            2    ,    |5|   ,    |7| | 10                                              

            ------------------------------------------------------------------------------------------



            


fundamental algo points :

        
        
        
        # these 2 states mean nothing behind robot since we have determined it is not good, or empty so functionally can remove 
        
        incoming wall 

        robot | wall , if wall in range , pop walls since none in left of robot 

        robot | wall cannot reach keep robot as it may stop bullet so simple add is ok
        wall | wall  add since cannot do anything 

        
        
        
        -----------------------------------------------------------------------
        incoming robot case 

        at this point we need to check if we can go to left and pop walls, if not remove everything since the robot is unoptimal
        we can keep a count of the walls to the right of the robot we can shoot, and check going back till not empty and count walls if they 
        are total more than or equal to on right then good we add that to result we can keep popping walls, in both case i think and 
        add them to result if the ones on left is greater or equal to right count 

        wall | robot : while can do and you have a wall keep popping walls (and wall is at top and not empty)
        we have empty | wall | robot
                robot | wall | robot
                far wall | robot
        in all 3 cases the robot will block for future robots so makes sense to truncate the things behind robot in both cases 
        if we have selected the robot to hit left >= right then remove the robot so it cannot be considered 
        else we keep the robot only for future 
        
        robot | robot : if popping and robot seen then add the robot or empty as well
        
        ------------------------------------------------------------------------------
        sort by the pos, 
        (pos, 'R' , dist , walls_on_right)   can check 1 index to see if wall or robot after sorting 
        (pos, 'W')


        sorted(['R', 'W'])   # ['R', 'W']
        we would want the reverse, W R


        
        to find the number of elements in a range
        [L , R ]

        bisect right(<= r) - bisect left( < l) 

        
        greedy does not work , need to try dp


        right query (will include walls at the ith position not the i + 1, since we cannot hit that point )
        # stop just before the next robot, include curr, query range on sorted walls

        [robot pos,             min(robot_pos + dist , robot_pos[i + 1] - 1) ]

        left query 
        # contain the current i but not i - 1,

        [max(robot_pos - dist , robot_pos[i - 1] + 1)                       ,robot pos]

        right[-1] = 0
        left[0] = 0
        
        for nums we define as the number of walls between consecutive robots, can include both 
        nums[0] = 0

        nums[i] = bw robots i and i - 1
        query [robot_pos[i -1 ] , robot_pos[i]] # will include walls at both positions i - 1 and i so note that


        dp[0][0]  = left[0] = 0
        dp[0][1] = right[0]


        dp[i][1] = max(
            dp[i - 1][0] + right[i],
            dp[i - 1][1] + right[i]
        )

        dp[i][0] = max(
            dp[i-1][0] + left[i],
            dp[i-1][1] - right[i - 1] + min(nums[i] , left[i] + right[i -1]) # open interval then fill with the max of the 2 
        )


"""
import collections
import bisect
from typing import List
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        nums = [0 for _ in range(0 , len(robots))] # num of walls between roboti , roboti - 1
        left = [0 for _ in range(0 , len(robots))] # walls able to destroy to the left of robot i
        right = [0 for _ in range(0 , len(robots))] # walls able to destroy to the right of robot i
        
        # key robots by the positon to map the distance
        robot_dist = {pos : dist for pos , dist in zip(robots , distance)}
        robots.sort() # sort we will index and record based on the sorted robots 
        walls.sort() # sort walls

        # iterate over each i and pos to fill data
        for index , robot_pos in enumerate(robots):
            d = robot_dist[robot_pos]
            # calculate right
            right[index] = bisect.bisect_right(walls, min(robot_pos + d , (robots[index + 1] - 1) if index + 1 < len(robots) else float("inf") )) - bisect.bisect_left(walls, robot_pos)
            
            # calculate left 
            left[index] = bisect.bisect_right(walls, robot_pos) - bisect.bisect_left(walls, max(robot_pos - d , (robots[index - 1] + 1) if index - 1 >= 0 else float("-inf") ))

            if index != 0:
                # calculate nums 
                nums[index] = bisect.bisect_right(walls, robot_pos) - bisect.bisect_left(walls, robots[index - 1])


        dp = collections.defaultdict(int)
        n = len(robots)

        # 0 - left, 1 - right
        dp[(0 , 0)] = left[0]
        dp[(0 , 1)] = right[0]

        for i in range(0  , n):
            dp[(i , 1)] = max(
                dp[(i - 1, 0)] + right[i],
                dp[(i - 1 , 1)] + right[i]
            )

            dp[(i , 0)] = max(
                dp[(i - 1 , 0)] + left[i],
                dp[(i  - 1, 1)] - right[i - 1] + min(nums[i] , left[i] + right[i - 1])
            )

        return max(dp[(n - 1 , 0)] , dp[(n - 1 , 1)])

