from typing import List
"""
Example 1:

Input: 
grid =

        1
      1 1 0
        1
      
        
        # identify each island
        # pick a start point on that island
        # try to expand in 4 directions , max( used 0 conversion if available (lock it for the downstream ))

        #  n * n * (constant)

        # dp ? 
        # for all 4 directions 
        # (i , j, used)
        # (i , j, not used)

        #    dirs 
        #    for all dir
        #    compute newx, newy 
        #       if 1 : -> unused 
        #       else  trasitions
        # dp[used, ]


[[1,0],
[0,1]]

Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = 

[[1,1],
[1,0]]

Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = 

[[1,1],
[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

        1
      1  1 1
        1
"""

import collections
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n , dirs = len(grid) , [ (-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1) ] 

        visited = set() # global for islands
        # island start -> {nodes mapping}
        islands = collections.defaultdict(set)
        # node to island mapping
        node_to_island = collections.defaultdict() 

        def dfs(ix , iy , x , y):
            islands[(ix , iy)].add((x , y))
            node_to_island[(x , y)] = (ix , iy)

            for dx, dy in dirs:
                newx ,  newy = x + dx , y + dy
                if 0 <= newx < n and 0 <= newy < n and (newx, newy) not in islands[(ix , iy)] and grid[newx][newy] == 1:
                    dfs(ix , iy , newx , newy)
        ans = 0
        for i in range(0 , n):
            for j in range(0 , n):
                if (i , j) not in visited and grid[i][j] == 1:
                    # start point of the island
                    islands[(i , j)] = set()
                    dfs(i , j , i , j)
                    ans = max(ans , len(islands[(i , j)]))
                    visited |= islands[(i , j)]
        
        # print(islands)
        # print("current max ans : " , ans)

        for i in range(0 , n):
            for j in range(0 , n):
                if (i , j) not in node_to_island:
                    # can flip and check
                    sub_ans = 1 # flip consideration
                    islands_covered = set() # to prevent duplicate islands
                    for di , dj in dirs:
                        newi , newj = i + di , j + dj
                        if 0 <= newi < n and 0 <= newj < n and (newi , newj) in node_to_island:
                            # print(islands[node_to_island[(newi , newj)]])
                            island_center = node_to_island[(newi , newj)]
                            if island_center in islands_covered:
                                # already visited
                                continue
                            islands_covered.add(island_center) # prevent duplicate
                            sub_ans += len(islands[island_center])
                    ans = max(ans , sub_ans)
        
        return ans


        