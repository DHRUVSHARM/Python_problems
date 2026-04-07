from typing import List
"""
0 is land
1 is water 


4dir land

closed island is all water surround

[0,0,1,1,0,1,0,0,1,0],
[1,1,0,1,1,0,1,1,1,0],
[1,0,1,1,1,0,0,1,1,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,0,0,1,1,1,0],
[0,1,0,1,0,1,0,1,1,1],
[1,0,1,0,1,1,0,0,0,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,0,0,1,0,1,0,1],
[1,1,1,0,1,1,0,1,1,0]


"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m , n , result , visited = len(grid) , len(grid[0]) , 0 , set()
        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        # return the (closed_island)
        def dfs(x , y):
            visited.add((x , y))

            water_surrounded = True # always in a land cell 

            for dx, dy in dirs:
                newx, newy = x + dx , y + dy
                if (newx, newy) not in visited:
                    if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 0:
                        # we still need the dfs to mark out stuff so use this carefully 
                        # so that the short circuit does not happen 
                        water_surrounded = dfs(newx , newy) and water_surrounded 
                    else:
                        # if out of boundary 
                        if not (0 <= newx < m and 0 <= newy < n ):
                            water_surrounded = water_surrounded and False
            
            return water_surrounded



        for row in range(0 , m):
            for col in range(0 , n):
                if (row , col) not in visited and grid[row][col] == 0:
                    closed = dfs(row , col)
                    if closed:
                        result += 1
        
        return result