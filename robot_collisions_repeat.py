"""
There are n 1-indexed robots,


each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, 

healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. 

If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, 

and the health of the other robot decreases by one. 

The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions,

 in the same order that the robots were given, i.e. final health of robot 1 (if survived),
  
final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

L |  L      same direction left

L | R       opp direction as good as a block 

both left cases dont matter 

R | L       L will collide with r 

R | R       store for the further things 

if collide, 
lower health remove 
other dec by one , surviivng still in same direction 

if same health both removed 

"""


from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # stack will store the indices in the end we can return the updated healths
        relative_indices = [index for index in range(0 , len(positions))]
        sorted_healths = [(pos , index , health , direction) for pos , health , direction , index in zip(positions , healths , directions , relative_indices)]
        sorted_healths.sort() # sort by the position 
        s = []

        for pos , ind , health, direction in sorted_healths:
            destroyed = False
            while len(s) and s[-1][1] == 'R' and not destroyed and direction == 'L':
                frontier_health = s[-1][0]
                if health < frontier_health:
                    destroyed = True
                    s[-1][0] -= 1
                    if s[-1][0] == 0:
                        s.pop() # remove the hit one 
                elif health > frontier_health:
                    s.pop()
                    health -= 1 # current one 
                    if health == 0:
                        destroyed = True
                else:
                    destroyed = True
                    s.pop() # remove both  

            if not destroyed:
                s.append([health , direction , ind])   

        s.sort(key=lambda element : element[2])
        return [health for health , _ , _ in s]