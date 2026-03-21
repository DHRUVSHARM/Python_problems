from typing import List

"""

grid = 

[
    [2,1,1],
    [1,1,0],
    [0,1,1]
]


0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

# total oranges rotten + nonrotten
# start at time = 0
# multi src bfs , level by level 
mark in visited, so that it is not rotten again 
we can check if the visited size == total oranges

"""

import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited, q , total_oranges , m , n , dirs  = set() , collections.deque() , 0 , len(grid) , len(grid[0]) , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        for row in range(0 , m):
            for col in range(0 , n):
                if grid[row][col] == 1 or grid[row][col] == 2:
                    total_oranges += 1
                    # also append the rotten oranges as the src node
                    if grid[row][col] == 2:
                        q.append((row , col))
                        # also add to the visit set 
                        visited.add((row , col))
        

        time = 0 # incremented at the end of each level 
        
        while len(q):
            level_size = len(q)

            while level_size:
                # this is a rotten orange now 
                x , y = q.popleft()
                for dx, dy in dirs:
                    newx, newy = x + dx , y + dy
                    # check if these are in range , not empty , and not visited (means rotten)
                    if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != 0 and (newx , newy) not in visited:
                        # we only add fresh oranges
                        visited.add((newx, newy)) # now rotten 
                        q.append((newx , newy))
                level_size -= 1
            
            if len(q):
                time += 1            


        # print(len(visited) , ":  " , total_oranges)
        return time if len(visited) == total_oranges else -1
