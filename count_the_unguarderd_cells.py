from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [["" for _ in range(n)] for _ in range(m)]

        for i , j in guards:
            grid[i][j] = 'G'

        for i , j in walls:
            grid[i][j] = 'W'

        
        seen , directions = set() , [(-1 , 0) , (1 , 0) , (0 , 1) , (0 , -1)]

        def check(i , j):
            for dx , dy in directions:
                new_i , new_j = i + dx , j + dy
                while 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != 'W' and grid[new_i][new_j] != 'G':
                    seen.add((new_i , new_j))
                    new_i += dx
                    new_j += dy


        for i , j in guards:
            check(i , j)

        return (m*n) - len(guards) - len(walls) - len(seen)