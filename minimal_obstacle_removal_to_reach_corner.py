import collections
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m , n , directions , seen = len(grid) , len(grid[0]) , [(-1 , 0) , (1 , 0) , (0 , 1) , (0 , -1)] , set([(0 , 0)])

        nodes = collections.deque([(0 , 0 , 0)])
        
        while len(nodes):
            dist , x , y = nodes.popleft()
            if x == m - 1 and y == n - 1:
                return dist
            
            for dx , dy in directions:
                newx , newy = x + dx , y + dy
                if 0 <= newx < m and 0 <= newy < n and (newx , newy) not in seen:
                    newdist = dist + grid[newx][newy]
                    if len(nodes) and newdist <= nodes[0][0]:
                        nodes.appendleft((newdist , newx , newy))
                    else:
                        nodes.append((newdist , newx , newy))
                    seen.add((newx , newy))

