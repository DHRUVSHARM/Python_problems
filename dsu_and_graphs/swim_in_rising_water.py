from typing import List
"""
swim in rising water

n square grid
i, j elevation 

t >= 0 

at time t - water level is t 

swim if nei has level  <= t 

you can swim as much in zero time, as long as the restrictions are applicable 

for every path you are trying to explore, you need to keep track of the max time from src to the dest target 
because that is the bottle neck 

monotonically increasing so greedy works 

(if you select a path that is greater in the beginning there is no way to reduce it down further )

src, target already there 

to reach src, you need grid value time as 0

reach destination stopping condition 

no need to keep track of all the distances

0 , 0 


                n - 1 , n - 1

"""

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited , q , result , n = set() , [(grid[0][0] , 0 , 0)] , -1 , len(grid) # Indicate unreachable error

        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        while len(q):
            frontier, u , v = heapq.heappop(q)
            if (u , v) not in visited:
                visited.add((u , v))
                if u == n - 1 and v == n - 1:
                    result = frontier
                    break

                # add the nei 
                for dx, dy in dirs:
                    newx, newy = u + dx , v + dy
                    if 0 <= newx < n and 0 <= newy < n and (newx,  newy) not in visited:
                        heapq.heappush(q , (
                            max(frontier , grid[newx][newy]),
                            newx,
                            newy
                            )) 

        return result 


