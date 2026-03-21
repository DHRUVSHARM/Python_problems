from typing import List

"""
You are given a map of a server center, 

represented as a m * n integer matrix grid, 

where 1 means that on that cell there is a server 

and 0 means that it is no server. Two servers are said to communicate 

if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.


1 0 
0 1


iterate through rows, if sum rows >= 2, add all the servers 
move through the row and flip 1 to -1 

move through each col, collect abs sum and umarked (1) if >= 2 at the end add the unmarked 
also can flip back to 1 on the way and add to keep the initial thing 

"""
# constant memory solution 
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid) , len(grid[0])
        result = 0

        for row in range(0 , m):
            if sum(grid[row]) < 2:
                continue
            
            result += sum(grid[row])
            for col in range(0 , n):
                if grid[row][col] == 1:
                    grid[row][col] = -1
    

        for col in range(0 , n):
            colsum , unmarked = 0 , 0
            for row in range(0 , m):
                if grid[row][col] == 1:
                    colsum += 1
                    unmarked += 1

                elif grid[row][col] == -1:
                    # flip and add but do not add to unmarked
                    grid[row][col] = 1
                    colsum += 1
                
            if colsum >= 2:
                result += unmarked
        

        return result