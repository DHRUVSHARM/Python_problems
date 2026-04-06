from typing import List

"""

    robot on an XY plane
    receive array of integers commands 

    three possible instructions 
    -2 : turn left 90 degrees
    -1 : turn right 90 degrees

    
       0,4
x = -y ,    x=y
        
        N
    
    W   R    E   
        
        S

        

        

        x , y => -y , x -> left
        x , y => y , -x  -> right

        x + dx , y + dy
        y + dx , -x + dy
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x , y) for x , y in obstacles)
        x , y , result , dir = 0 , 0 , 0 , 'N' # initial dir 

        # command mapping , initial direction is N , we have diff, left dir, right dir 
        command_map = {
            'N' : [(0 , 1), 'W' , 'E'],
            'S' : [(0 , -1), 'E' , 'W'],
            'E' : [(1 , 0),  'N' , 'S'], 
            'W' : [(-1 , 0), 'S' , 'N']
        }

        for command in commands:
            diff, left, right = command_map[dir]
            dx , dy = diff
            if command == -2:
                # left
                dir = left
            elif command == -1:
                # right
                dir = right
            else:
                # atmost 9 walk since range is 1 to 9 
                steps = command
                while steps and (x + dx , y + dy) not in obstacles:
                    
                    x += dx
                    y += dy
                    steps -= 1
                
                result = max(result , x**2 + y**2)
                

        return result 




