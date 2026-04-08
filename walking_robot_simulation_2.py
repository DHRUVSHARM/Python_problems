from typing import List

"""
(0 , 3)                 (6 , 3)

        3 , 1           (6 , 1)
(0 , 0)                 (6 , 0)
start here 

coordinates are also , width height ie ; x . y

init with : width , height -> (6 , 3)

    ob
ob   r   ob
    ob

# the way the question is made we can atleast go back and retrace 



    4 steps             5 steps
 2,0           2 , 4               2 , 9


 100 steps ? 

 100 % 9 = 1

 steps -= 100 
"""


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width # ( 0 <= x < width) 
        self.height = height # ( 0 <= y < height)
        self.x = 0
        self.y = 0
        self.direction = 'E'
        # init position and direction 

        self.diff = { 'N' : (0 , 1), 'E' : (1 , 0), 'S' : (0 , -1), 'W' : (-1 , 0)}
        self.left = { 'N' : 'W', 'E' : 'N', 'S' : 'E', 'W' : 'S'} # move counterclockwise 
        self.plain_direction = {'N' : "North" , 'E' : "East" , 'W' : "West" , 'S' : "South"}
        self.perimeter = 2 * (self.height - 1 + self.width - 1) # we are counting steps 
        # east to east clock 

    def step(self, num: int) -> None:
        # will move num steps one by one , there is no obstacle but there is a constraint on 
        # going out of bounds 
        # TC : (10**5 // 10**2) * 10*4
        
        steps = num # remaining steps they are atleast 1 

        # need to write this in a nice way 
        cx , cy , steps = self.x , self.y , num

        # to calculate new position effeciently
        # ( x , y )             min(x + steps_rem , width - 1) , y
        # old                   # new 
        while steps:
            if self.y == 0 and steps >= self.perimeter:
                # same end, direction , just skip perimeter 
                steps = steps % self.perimeter
                # position is back to the same one 
                # direction will be changed 3 times 
                # this will depend on where we are
                # ultimately we will come back to a state where the thing starts from the bottom line somewhere
                if self.x == 0:
                    if self.direction == 'E':
                        self.direction = 'S'
                    elif self.direction == 'S':
                        pass
                    else:
                        raise Exception
                else:
                    # will come back to same direction
                    # do nothing 
                    pass

            else:
                # normal traversal for the remainder 
                if self.direction == 'E':
                    cx , cy = min(self.x + steps , self.width - 1) , self.y
                    steps -= abs(cx - self.x)
                elif self.direction == 'W':
                    cx , cy = max(self.x - steps , 0) , self.y
                    steps -= abs(cx - self.x)
                elif self.direction == 'N':
                    cx , cy = self.x , min(self.y + steps , self.height - 1)
                    steps -= abs(cy - self.y)
                else:
                    cx , cy = self.x , max(self.y - steps , 0)
                    steps -= abs(cy - self.y)


                # assign the current to the traversed
                self.x , self.y = cx , cy

                # need to change direction only if the steps are complete and we are at a boundary  
                if steps != 0:
                    # change direction for next loop  
                    self.direction = self.left[self.direction]


        # at the end the final position and direction is correctly assigned 


    def getPos(self) -> List[int]:
        return [self.x , self.y]

    def getDir(self) -> str:
        return self.plain_direction[self.direction] 


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()