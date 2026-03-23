"""
You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

Return the length of the shortest path from the top-left corner 
of Grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells.

Note:

If there is no such path, return -1.
The length of a path is the number of moves from the starting cell to the ending cell.
Example 1:

Input: grid = [
  [0, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0]
]

Output:
6

1   1

1   0

simple walk with obstacles around so we use bfs
if not path we return -1 (possible)
verical horizontal move allowed only
bfs layer by layer (will visit each cell once) we can again do without hashset and mark the visited as 1 ?
we cannot i think



1   1   1   1   1  1   
    1       1
    1   1   1 

"""

from typing import List

import collections
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m , n , result = len(grid) , len(grid[0]) , -1 # need to reach the bottom right corner
        if not (m > 0 and n > 0) or grid[0][0] == 1:
            # invalid cases 
            return -1
        
        # shortest path we want to reach the result once
        q , dirs = collections.deque([(0 , 0 , 0)]) , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        while len(q):
            x , y , w = q.popleft()
            if x == m - 1 and y == n - 1:
                result = w
                break
            
            # since we have considered this 
            # and also we have gone through this one time , if it is a previous node no point in considering
            # the other thing is we have considered the path previously in the shortest way 
            # so any other longer way is wrong and if this is invalid then that longer way is invalid as well
            for dx , dy in dirs:
                newx, newy = x + dx , y + dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 0:
                    # mark as visited
                    grid[newx][newy] = 1
                    q.append((newx , newy , w + 1))    
            
        
        # will default to -1 
        return result


        
