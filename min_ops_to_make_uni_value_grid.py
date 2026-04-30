# median solution 
"""
from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # grid = [[2,4],[6,8]], x = 2
        # median , will be the best point to move to 
        # only same modularity values can be made into common value 
        m , n = len(grid) , len(grid[0])
        
        flat , parity = [] , None
        for i in range(0 , m):
            for j in range(0 , n):
                if parity is None:
                    parity = grid[i][j] % x
                else:
                    if parity != grid[i][j] % x:
                        return -1
        
                flat.append(grid[i][j])
        
        # find median
        flat.sort()

        ans , target = 0 , flat[len(flat) // 2]

        for element in flat:
            ans = ans + abs(element - target) // x
        
        return ans
"""


# prefix, suffix sum solution, will still require sorting 
# [1]
# [1]
from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        parity , m , n , flat = None , len(grid) , len(grid[0]) , []

        for i in range(0 , m):
            for j in range(0 , n):
                if parity is None:
                    parity = grid[i][j] % x
                else:
                    if parity != grid[i][j] % x:
                        return -1
        
                flat.append(grid[i][j])
        
        flat.sort()
        prefix , suffix , p_sum , s_sum = [0]*len(flat) , [0]*len(flat) , 0 , 0


        # print(flat)
        for index in range(0 , len(flat)):
            p_sum += flat[index]
            s_sum += flat[len(flat) - index - 1]
            prefix[index] = p_sum
            suffix[len(flat) - index - 1] = s_sum

        # print(suffix)
        #  print(prefix)
        # check every case
        result = float("inf")

        # 
        for index , element in enumerate(flat):
            # print("element : " , element)
            # print("result : " ,  element * (2*index - len(flat) + 1) - (prefix[index - 1] if (index - 1 >= 0) else 0) + (suffix[index + 1] if (index + 1 < len(flat)) else 0 ))
            result = min(
                result,
                (element * (2*index - len(flat) + 1) - (prefix[index - 1] if (index - 1 >= 0) else 0) + (suffix[index + 1] if (index + 1 < len(flat)) else 0 )) // x
            )

        return result