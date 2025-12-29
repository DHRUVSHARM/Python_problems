from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # first we need to find at least 1 island
        
        dirs , m , n = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)] , len(grid) , len(grid[0])
        src_island , visited = [] , set()
      
        def dfs(i , j):
            island = []
            island.append((i , j))
            visited.add((i , j))

            for dx , dy in dirs:
                newx , newy = i + dx , j + dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] and (newx , newy) not in visited:
                    sub_island = dfs(newx , newy)
                    island.extend(sub_island)

            return island 

      

        for i in range(0 , m):
            for j in range(0 , n):
                if grid[i][j] and (i , j) not in visited:
                    # find atleast one island
                    src_island = dfs(i , j)
                    # since we found one, we can break here 
                    break
        
        
        # now to find the shortest path we will have to do a multisource bfs
        visited = set(src_island)
        src_island = list(map(lambda element : (element , 0) , src_island)) 
        q , level_size = deque(src_island) , len(src_island)
        
        while q:
            while level_size:
                node, bridge_size = q.popleft()
                i , j = node

                for dx , dy in dirs:
                    newx, newy = i + dx , j + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx , newy) not in visited:
                        if grid[newx][newy]:
                            return bridge_size
                        q.append(((newx , newy) , bridge_size + 1))
                        visited.add((newx , newy))

                level_size -= 1
            
            level_size = len(q)


    if __name__ == "__main__":
        arr = [(1 , 1) , (1 , 1) , (1 , 1) , (1 , 1)]
        arr = list(map(lambda element : (element , 0) , arr))

        print(arr)
        

        
