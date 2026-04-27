from typing import List

"""
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


            no
     1      1       1
            no

            1 : l , r
            2 : u , d



(0 , 0)




                        (m - 1 , n - 1)

"""


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m , n = len(grid) , len(grid[0])
        visited = set()

        def dfs(x , y):
            visited.add((x , y))
            if x == m - 1 and y == n - 1:
                return True

            ans = False
            # find valid neighbours
            if grid[x][y] == 1:
                dirs = [(0 , 1) , (0 , -1)]
                # check right, left
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # right
                            if grid[newx][newy] in {1 , 3 , 5}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # left 
                            if grid[newx][newy] in {1 , 4 , 6}:
                                ans = ans or dfs(newx , newy)


            elif grid[x][y] == 2:
                dirs = [(-1 , 0) , (1 , 0)]
                # check up, down
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # up
                            if grid[newx][newy] in {2 , 3 , 4}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # down
                            if grid[newx][newy] in {2 , 5 , 6}:
                                ans = ans or dfs(newx , newy)


            elif grid[x][y] == 3:
                dirs = [(0 , -1) , (1 , 0)]
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # left 
                            if grid[newx][newy] in {1 , 4 , 6}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # down 
                            if grid[newx][newy] in {2 , 5 , 6}:
                                ans = ans or dfs(newx , newy)

            
            elif grid[x][y] == 4:
                dirs = [(0 , 1) , (1 , 0)]
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # right
                            if grid[newx][newy] in {1 , 3 , 5}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # down 
                            if grid[newx][newy] in {2 , 5 , 6}:
                                ans = ans or dfs(newx , newy)

            elif grid[x][y] == 5:
                dirs = [(0 , -1) , (-1 , 0)]
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # left
                            if grid[newx][newy] in {1 , 4 , 6}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # up
                            if grid[newx][newy] in {2 , 3 , 4}:
                                ans = ans or dfs(newx , newy)

            else:
                dirs = [(0 , 1) , (-1 , 0)]
                for index, element in enumerate(dirs):
                    dx , dy = element
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                        if index == 0:
                            # right 
                            if grid[newx][newy] in {1 , 3 , 5}:
                                ans = ans or dfs(newx , newy)
                        else:
                            # up
                            if grid[newx][newy] in {2 , 3 , 4}:
                                ans = ans or dfs(newx , newy)

            return ans

        result = dfs(0 , 0)
        return result