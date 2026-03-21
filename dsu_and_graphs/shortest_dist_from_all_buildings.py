from typing import List
"""
1 : buidling 
0 : empty  
2 : obstacle

# maps

single visited 
reset 
call bfs

src node in bfs helper signature 

map all 0's 
[0 , 0]
node (0) -> [buildings touched, dist total]


"""
import collections
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m , n , visited , node_mapping , building_count , dirs = len(grid) , len(grid[0]) , set() , {} , 0 , [(-1 , 0) , (0 , -1) , (1 , 0) , (0,  1)]

        def bfs(sx , sy):
            # src is a building so no need to mark visited 
            q = collections.deque([(sx , sy , 0)])

            while len(q):
                x , y , dist = q.popleft()

                for dx , dy in dirs:
                    newx, newy = x + dx , y + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx , newy) not in visited and grid[newx][newy] == 0:
                        visited.add((newx, newy))
                        if (newx , newy) not in node_mapping:
                            # buildings touched, dist 
                            node_mapping[(newx , newy)] = [0 , 0]
                        node_mapping[(newx , newy)][0] += 1
                        node_mapping[(newx , newy)][1] += (dist + 1)
                        # add for further
                        q.append((newx , newy , dist + 1))


        # iterate over the buildings
        for i in range(0 , m):
            for j in range(0 , n):
                if grid[i][j] == 1:
                    # each building will reach once 
                    building_count += 1
                    # start bfs with reset visited 
                    visited = set()
                    bfs(i , j)
        
        min_dist = float("inf")
        for node, data in node_mapping.items():
            buildings, distance = data
            if buildings == building_count:
                # all buildings reachable 
                min_dist = min(min_dist , distance)

        return -1 if min_dist == float("inf") else min_dist 
