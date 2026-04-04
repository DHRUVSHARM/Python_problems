"""
Input: encodedText = "iveo    eed   l te   olc", rows = 4



    0   1   2   3   4   5  
0   f   d   f   f   
1       f   d   f   f
2           f   d   f  f
3               f  d   f  


offset from 0 to rows - 1

0 <= col - row <= (rows - 1)

col [row , row + rows - 1]

row: 0         0 , 0 + 3 
row : 1        1 , 1 + 3
row: 2         2 , 2 + 3
row: 3         3 , 3 + 3

so max col will be rows - 1 + rows - 1
= 6


note rows is row count

cols = 2 * (rows - 1)
rows = rows

fill each with < rows

for r in 0 , rows:
    for c in r , r + rows:
        fill r,c

jagged traversal 

for off in (0 , m):
    for row in (0 , m):
        while index < n and and grid[row][index] is not None:
            add to result
            grid[row] 
            index += 1

            
for row 

then 

row <= col <= rows

00  10
    11  12
        22  13
            33  14

_
_ _
_ _ _

"""

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # first we need to get the initial matrix 
        m , n = rows, len(encodedText) // rows
        grid = [[None for _ in range(n)] for _ in range(m)]
        print(n)

        if len(encodedText) == 0:
            # empty base case 
            return ''
        
        index = 0

        for row in range(0 , m):
            for col in range(0 , n):
                grid[row][col] = encodedText[index]
                index += 1


        # once we have we need to diagonal traversal and build the output 
        result = []

        for offset in range(0 , n):
            row , col = 0 , 0
            while row < m and col + offset < n:
                result.append(grid[row][col + offset])
                row += 1
                col += 1

        while len(result) and result[-1] == " ":
            result.pop()

        return ''.join(result)