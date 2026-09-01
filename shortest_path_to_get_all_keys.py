from typing import List

"""
. is an empty cell
# is a wall 
@ is the starting point 

lowercase represents keys
uppercase represents locks 

Each key in the grid is unique.
Each key in the grid has a matching lock.



1   1   1   1   1   1  

"""

import collections
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m , n = len(grid) , len(grid[0])

        # we will use a mask to represent the state of the keys collected 
        # NOTE: the idea is to collect all the keys, not open all the locks 
        # initial mask will have 1 representing key not collected
        # aim : make the mask 0 


        sx , sy = -1 , -1
        keys_collected = 0

        # since the characters are contiguous the ordinal positions of the chars can be used to make the mask 
        # checking existence will also be similar, since the current active 
        # NOTE : we can collect multiple keys 
        # The number of keys in the grid is in the range [1, 6].
        # if k = 3 , means we will have 111 = (1 << keycount) - 1

        for i in range(0 , m):
            for j in range(0 , n):
                if grid[i][j] == '@':
                    sx , sy = i , j
                elif 'a' <= grid[i][j] <= 'z':
                    # keys seen 
                    keys_collected += 1 

        # we know final state required
        target = (1 << keys_collected) - 1
        # print("target : " , target)

        # state will be x , y , key_collected mask (initially 0)
        # reaching somewhere with less or equal number of keys can be ignored 

        dp = [[None for _ in range(0 , n)] for _ in range(m)]
        q = collections.deque([(sx , sy , 0 , 0)]) 
        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        while len(q):
            x , y , mask , steps = q.popleft()
            # print(x , y , mask , steps)
            if mask == target:
                return steps

            for dx, dy in dirs:
                newx, newy, new_mask, new_steps = x + dx , y + dy , mask , steps + 1
                if (0 <= newx < m) and (0 <= newy < n):
                    if grid[newx][newy] == '#':
                        # blocked
                        continue
                    elif 'a' <= grid[newx][newy] <= 'z':
                        # collect keys
                        new_mask = new_mask | (1 << (ord(grid[newx][newy]) - ord('a')))
                    elif 'A' <= grid[newx][newy] <= 'Z':
                        req_key_mask = 1 << (ord(grid[newx][newy]) - ord('A'))
                        if (req_key_mask & new_mask) == req_key_mask:
                            # req key exists, we can stay on this lock position and open it 
                            pass
                        else:
                            continue
                    else:
                        # older states, empty etc; are already handled
                        # print("here")
                        pass

                    # now we check if we have reached this position before with equal or more keys
                    # we check if bigger_mask | smaller mask or equal = bigger_mask  means we already have a better state 
                    # smallest state is 0 that is why we choose as sentinel value 
                    
                    if dp[newx][newy] is not None and (dp[newx][newy] | (new_mask) == dp[newx][newy]):
                        pass
                    else:
                        dp[newx][newy] = new_mask
                        q.append((newx, newy , new_mask, new_steps))

        return -1 