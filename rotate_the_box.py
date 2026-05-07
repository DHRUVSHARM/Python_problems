from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m , n = len(boxGrid) , len(boxGrid[0])

        for row in range(0   , m):
            last_space_seen = n
            # print("row : " , row)
            for col in range(n - 1 , -1 , -1):
                # print(last_space_seen)
                if boxGrid[row][col] == '.' and last_space_seen == n:
                    # empty
                    last_space_seen = col # store
                elif boxGrid[row][col] == '#' and last_space_seen != n:
                    # stone and can swap
                    # swap, increment and update the space 
                    # print("swapping ")
                    boxGrid[row][col] , boxGrid[row][last_space_seen] = boxGrid[row][last_space_seen] , boxGrid[row][col]
                    last_space_seen -= 1

                elif boxGrid[row][col] == '*':
                    # block , skip 
                    last_space_seen = n # spaces before clear 
        
        # n m 
        result = [[None for _ in range(0 , m)] for _ in range(0 , n)]
        for i in range(0 , m):
            for j in range(0 , n):
                result[j][m - i - 1] = boxGrid[i][j]
        
        return result