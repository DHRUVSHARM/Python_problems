from typing import List 
class Solution:
             
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m , n = len(grid) , len(grid[0])
        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]
        visited = set()

        # since this is an undirected graph , we will need to maintain a parent to not misclassify 
        # and also will work only if length is 3 or more, in our case we will have cycle of length atleast 4
        # since the movement is 4 directional 
        def dfs(node, parent, letter):
            # more simpler we check if neighbour is visited and and is not parent then that means cycle atleast 3 size 
            visited.add(node)
            x , y = node

            for dx, dy in dirs:
                newx, newy = x + dx , y + dy
                if (newx , newy) in visited and (newx , newy) != parent and grid[newx][newy] == letter:
                    # we are able to reach the same node from 2 different ways, 
                    # and it is not the direct parent implies cycle 
                    return True
                
                if (newx , newy) not in visited and 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == letter:
                    subans = dfs((newx , newy) , node, letter)
                    if subans:
                        return True
            
            return False
            

        for r in range(0 , m):
            for c in range(0 , n):
                if (r , c) not in visited:
                    ans = dfs((r , c) , None, grid[r][c]) 
                    if ans == True:
                        return True
        
        return False