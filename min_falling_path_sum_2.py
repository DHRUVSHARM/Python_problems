from typing import List


"""
Given an n x n integer matrix grid, 
return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts 
is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

non zero shifts 
square grid 

at a point we need 

the minimum from the next row excpet the same col 
how to calculate while running and in const time lookup ?

at the last row it will always be the value itself

at the end we will just take the min from the first row 



"""
import collections
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result , minimal_two , prev_minimal_two = float("inf") , collections.deque() , collections.deque()

        for row in range(n - 1 , -1 , -1):
            for col in range(0 , n):
                    
                if row == n - 1:
                    pass # keep the same 
                else:
                    # iterate through the deque and get the ans (sorted)
                    subans = 0 # atleast one guaranteed since n = 1
                    for value, c in prev_minimal_two:
                        if c != col:
                            subans = value
                            break
                    
                    grid[row][col] += subans
                
                # calculate the current minimal for next iteration , these are the path sums that have been changed  
                if len(minimal_two) == 0:
                    minimal_two.append((grid[row][col] , col))
                elif len(minimal_two) == 1:
                    if minimal_two[0][0] <= grid[row][col]:
                        minimal_two.append((grid[row][col] , col))
                    else:
                        minimal_two.appendleft((grid[row][col] , col))
                else:
                    if grid[row][col] >= minimal_two[-1][0]:
                        pass
                    elif minimal_two[-1][0] > grid[row][col] >= minimal_two[0][0]:
                        minimal_two.pop()
                        minimal_two.append((grid[row][col] , col))
                    else:
                        minimal_two.appendleft((grid[row][col] , col))
                        minimal_two.pop()

            # store for the next row 
            prev_minimal_two = minimal_two.copy()
            # empty for the next row 
            minimal_two = collections.deque([])

            # print(prev_minimal_two)
            # print(minimal_two)

        result = min(grid[0])
        return result



# [] , [1 , 2]
# 