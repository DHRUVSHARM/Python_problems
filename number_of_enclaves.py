"""
true if any component, 
and the number of land cells (atleast one)

else false

add land cells, from where we get false

is_enclave , size

"""

from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m , n , visited , result , dirs = len(grid) , len(grid[0]) , set() , 0 , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        def dfs(x , y):
            visited.add((x , y))
            size = 1
            reach = False

            for dx , dy in dirs:
                newx, newy = x + dx , y + dy
                if (newx , newy) not in visited:
                    if (0 <= newx < m and 0 <= newy < n) and grid[newx][newy] == 1:
                        # can move and adjacent is land cell 
                        sub_reach , sub_size = dfs(newx , newy)
                        size += sub_size
                        reach = reach or sub_reach
                    else:
                        # can reach boundary adjancent is boundary or we have water cell
                        if not (0 <= newx < m and 0 <= newy < n):
                            # out of boundary 
                            reach = True
                        
            
            return reach , size

        for i in range(0 , m):
            for j in range(0 , n):
                if (i , j) not in visited and grid[i][j] == 1:
                    reach_boundary , size = dfs(i , j)
                    if not reach_boundary:
                        result += size
        

        return result