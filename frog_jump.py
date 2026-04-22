"""

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by
 jumping 1 unit to the 2nd stone, 
 then 2 units to the 3rd stone, 
 then 2 units to the 4th stone, 
 then 3 units to the 6th stone, 
 4 units to the 7th stone, 
 and 5 units to the 8th stone.
       
 
 T      T   
 [0,    1,  3,  5,  6,  8,  12,     17]

 

 dp[0] = {1} # can reach from 0 
 dp[1] = {1 , 3 , 2} 
 dp[3] = {}
    go back get diff, 
 
for all jumps sizes
dp[pos][somejumpsize] = dp[pos - somejumpsize][pos - somejumpsize] or dp[pos - sjz][pos - sjz - 1] or dp[pos - sjz][pos - sjx + 1]


dp[0][0] = true

dp[2][2] ? dp[0][2 -1] or dp[0][2] or dp[0][2 + 1]
dp[1][1] ? dp[0][0] or dp[0][1] or dp[0][2]

 k =1
 1 + 1 = 2
 1 + 2 = 3
 1 + 0 = 1



 ------------- try this ? 
k is ove 0 ... i - 1 diff , get out of bound will be False , n2 solution and we store the values behind  
 dp[i] = dp[i - k] and (dp[i - k - k] or dp[i - k - (k = 1)] or dp[i - k - (k + 1)])

 

dp[0][0] = true

dp[2][2] ? dp[0][2 -1] or dp[0][2] or dp[0][2 + 1]
dp[1][1] ? dp[0][0] or dp[0][1] or dp[0][2]



0   1   3
0   0      
"""
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        """
        dp = {}
        dp[(0 , 0)] = True

        result = False

        for index in range(1 , len(stones)):
            curr_pos = stones[index]
            # since the jumps are diff, so does not matter currpos , diff combinations will be diff, since we have strictly increasing 
            for prev_index in range(index - 1 , - 1 , -1):
                prev_pos = stones[prev_index] 
                diff = curr_pos - prev_pos
                if diff - curr_pos > 2:
                    break

                dp[(curr_pos , diff)] = dp.get((prev_pos , diff) , False) or dp.get((prev_pos , diff - 1) , False) or dp.get((prev_pos , diff + 1) , False)
        
                if index == len(stones) - 1:
                    result = result or dp[(curr_pos , diff)]
        
        return result
        """

        # too much repeated states and tle with normal dp
        # iterative building dfs approach will work and we will keep only pruned paths for this problem  
        # only true states will be pushed so number of states will be very small
        s , visited = [(0 , 0)] , set([(0 , 0)])
        valid_stones = {stone : index for index, stone in enumerate(stones)}
        # iterative dfs
        while s:
            
            curr_pos , diff = s.pop()
            # print(curr_pos , " : " , diff)
            if curr_pos == stones[-1]:
                return True

            for d_diff in [diff - 1 , diff , diff + 1]:
                if d_diff < 0:
                    continue
                new_pos = curr_pos + d_diff
                if new_pos in valid_stones and (new_pos , d_diff) not in visited:
                    visited.add((new_pos , d_diff))
                    s.append((new_pos , d_diff))
            

        return False
