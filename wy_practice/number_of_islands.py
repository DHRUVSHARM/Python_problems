from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        # connected components starting from islands that have 1 

        visited , count , dirs = set() , 0 , [(-1 , 0) , (0 , -1) , (0 , 1) , (1 , 0)]

        def dfs(i , j):
            visited.add((i , j))
            for di , dj in dirs:
                new_i , new_j = i + di , j + dj
                if 0 <= new_i < m and 0 <= new_j < n and (new_i , new_j) not in visited and grid[new_i][new_j] == "1":
                    dfs(new_i , new_j)


        for i in range(0 , m):
            for j in range(0 , n):
                if grid[i][j] == "1" and (i , j) not in visited:
                    # island found
                    count += 1
                    dfs(i , j)
        
        return count


        