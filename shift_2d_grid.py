"""

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 


    0       1       2
0   _       1       2

1   3       _       5

2   6       7       _

3   9       10      11



m = 4
n = 3


index 2d = r , c
    to
index 1d =  n*r + c 

shift k, 


(index 1d + k) % mn


index 1d % n = (n*r + c) % n = c
index 1d // n = (n*r + c) // n = r (n > c always so c // n = 0

say 10 = (10 // 3) , (10 % 3) = 3, 1

"""

from typing import List 

# optimized tc + no auxillary memory solution 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])
        shifts = 0
        total = m * n
        start = 0 # starting 1d index 

        while shifts < total:
            
            prev = grid[start // n][start % n]
            # we go from start to the next
            index = start 

            while True:

                new_index = (index + k) % total 
                new_prev = grid[new_index // n][new_index % n]

                grid[new_index // n][new_index % n] = prev
                prev = new_prev

                shifts += 1
                
                index = new_index
                if index == start:
                    break

            start += 1 # try with new offset , this works since the indices have been flattened into a single dimension 


        return grid


"""
# optimized index + extra memory solution 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])

        new_grid = [[None for _ in range(n)] for _ in range(m)]

        for i in range(0 , m):
            for j in range(0 , n):
                # i , j => new_i , new_j
                index = (n*i + j + k) % (m*n)
                new_i , new_j = index // n , index % n
                new_grid[new_i][new_j] = grid[i][j]

        return new_grid
"""



"""
# naive solution with k shifts 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # brute force
        m , n = len(grid) , len(grid[0])
        while k:
            prev = grid[-1][-1]
            
            for i in range(0 , m):
                for j in range(0 , n):
                    # pick the current one 
                    temp = grid[i][j]
                    # fix the correct one 
                    grid[i][j] = prev
                    prev = temp
            
            k -= 1
        
        return grid
"""