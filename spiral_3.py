from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = {
            0 : ['R' , (0 , 1)],
            1 : ['D' , (1 , 0)],
            2 : ['L' , (0 , -1)],
            3 : ['U' , (-1, 0)],
        }
        
        visited = set()
        i , j = rStart , cStart

        level , change , index = 1 , 0 , 0
        
        ans = []

        def move(index , i , j):
            if 0 <= i < rows and 0 <= j < cols and (i , j) not in visited:
                ans.append([i , j])
                visited.add((i , j))

            step = 0
            di , dj = directions[index][1]

            while step < level:
                i , j = i + di , j + dj
                if 0 <= i < rows and 0 <= j < cols and (i , j) not in visited:
                    ans.append([i , j])
                    visited.add((i , j))
                
                step += 1
            
            return i , j


        while len(visited) < rows*cols:
            i , j = move(index , i , j)
            index = (index + 1) % 4
            change += 1
            if change == 2:
                level += 1
                change = 0
        
        return ans


        
