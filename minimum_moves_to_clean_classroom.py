from typing import List

"""


'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space


"""

import collections
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m , n = len(classroom) , len(classroom[0])
        index_counter_map , counter = {} , 0

        sx , sy = -1 , -1 # start point 

        for i in range(0 , m):
            for j in range(0 , n):
                if classroom[i][j] == 'S':
                    sx , sy = i , j
                elif classroom[i][j] == 'L':
                    index_counter_map[(i , j)] = counter # there are atmost 10 iitter in the grid 
                    counter += 1

        # bfs state will be (i, j, litter_map, energy_rem, steps)
        q = collections.deque([(sx , sy , 0 , energy , 0)])
        # we can also prevent and not use visited and prune some states 
        # if we reach a state (sx , sy, litter_map) and dp[sx][sy][litter_map] >= current state
        # then there is no need to use it, since in bfs we guarantee curr_steps > current state steps
        # so if even with more steps, we cannot have as much energy at this point, (or equal , in which case it does not mattter)
        # there is no need to enqueue and consider this state again 
        # loops are also broken since curr (e) -> next (e - 1) -> curr(e - 2) [will not be considered]
        # in case curr (e)(R) -> next (e - 1) -> curr(e - 1 to e) -> next (again e - 1 , but we will ignore since we ignore equal cases)
        # as well.  

        mask_variations = 2**10
        dp = [[[float("-inf") for _ in range(0 , mask_variations)] for _ in range(0 , n)] for _ in range(0 , m)]
        # dp[x][y][mask] 
        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        while len(q):
            # print(q)
            x , y , mask , e , curr_steps = q.popleft()
            if mask == ((1 << (counter)) - 1 ):
                # we know this will be valid energy state atleast 0
                # and is least steps due to nature of bfs
                return curr_steps

            for dx , dy in dirs:
                newx , newy = x + dx , y + dy
                new_mask, new_energy, new_steps = mask, e - 1, curr_steps + 1
                if 0 <= newx < m and 0 <= newy < n and new_energy >= 0:
                    # new state calculation 
                    if classroom[newx][newy] == 'R':
                        # reset
                        new_energy = energy
                    elif classroom[newx][newy] == 'L':
                        # collect litter
                        new_mask = new_mask | (1 << index_counter_map[(newx , newy)])
                    elif classroom[newx][newy] == 'X':
                        # not included
                        continue
                    else:
                        # will handle S, or empty or revisited states
                        pass

                    if dp[newx][newy][new_mask] >= new_energy:
                        # previously have better or same state
                        pass
                    else:
                        dp[newx][newy][new_mask] = new_energy
                        q.append((newx, newy, new_mask , new_energy , new_steps))

        return -1 # could not reach valid state 
        
                
        
