"""

k = 4 , n = 4, at 4th rotation we will not have anything 
1 2 3 4

so k % n rotations, k % array len rotations to reduce steps complexity 


      sc  ec  
sr    10 20 
er    40 30 

after traversal 
traversal

start at (er , ec)

up (-1 , 0) till row = sr
left(0 , -1) till col = sc
down (1 , 0) till row = er
right (0 , 1) till col = ec # back ro er, ec

all the while , start with prev = - 1
# if -1 dont put 
otherwise put and take current as the next one 

start from m - 1 , n - 1
    m -= 1, n -= 1

sr, sc , er, ec
0 , 0 , m - 1 , n - 1

while er - sr  > 0 and ec - sc > 0:
    do 
    sr += 1, er -= 1 , sc += 1, ec -= 1


# at every iteration 

        sc      ec
sr

er

"""

from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])
        sr , er , sc , ec  = 0 , m - 1 , 0 , n - 1

        def traverse(sr , sc , er , ec):
            n = 2*(er - sr + 1) + 2*(ec - sc + 1) - 4 
            nonlocal k 
            steps = k % n # reduced rotations
            # print("new k : " , k)
            
            """
            start at (er , ec)
            up (-1 , 0) till row = sr
            left(0 , -1) till col = sc
            down (1 , 0) till row = er
            right (0 , 1) till col = ec # back ro er, ec
            """
            while steps:
                row , col  = er , ec
                prev = -1
                while row >= sr:
                    temp = grid[row][col] # for prev 
                    if prev !=- 1:
                        grid[row][col] = prev
                    prev = temp
                    row -= 1
                
                row = sr # reset
                col -= 1

                while col >= sc:
                    temp = grid[row][col]
                    if prev != -1:
                        grid[row][col] = prev
                    prev = temp
                    col -= 1
                
                col = sc
                row += 1

                while row <= er:
                    temp = grid[row][col]
                    if prev != -1:
                        grid[row][col] = prev
                    prev = temp
                    row += 1
                
                row = er
                col += 1

                while col <= ec:
                    temp = grid[row][col]
                    if prev != -1:
                        grid[row][col] = prev
                    prev = temp
                    col += 1
                steps -= 1


        while er - sr > 0 and ec - sc > 0:
            traverse(sr , sc , er , ec)
            sr += 1
            er -= 1
            sc += 1
            ec -= 1

        return grid


        
        

