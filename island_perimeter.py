from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols , dirs ,visited = len(grid) , len(grid[0]) , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)] , set()

        def dfs(node):
            # we only visit valid areas 
            visited.add(node)
            x , y = node

            perimeter = 0
            for dx , dy in dirs:
                newx , newy = x + dx , y + dy
                if (newx , newy) not in visited:
                    if (0 <= newx < rows) and (0 <= newy < cols) and grid[newx][newy] == 1:
                        # we need to consider the count from here and add it to total 
                        perimeter += dfs((newx, newy))
                    else:
                        # the neighbour is out of bounds or and edge shared with water, contributes 1
                        perimeter += 1
            
            return perimeter

        
        result = 0
        for i in range(0 , rows):
            for j in range(0 , cols):
                if (i , j) not in visited and grid[i][j] == 1:
                    # we found the island and calculate
                    result = dfs((i , j))
        

        return result
    