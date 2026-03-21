from typing import List

"""
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# row hashset , new per row  -> early return 
# col indexed dict   -> early return 
# 

row , col -> row // 3 , col //3
maintain a dictionary -> duplicates early return  
00              03              06
30              33              36
60              63              66

00 -> 22        03 -> 25        06 -> 28

[["5","3",".",  ".","7",".",    ".",".","."]
,["6",".",".",  "1","9","5",    ".",".","."]
,[".","9","8",  ".",".",".",    ".","6","."]


,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]

,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


"""
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_row , col_mapping , box_mapping = set() , collections.defaultdict(set) , collections.defaultdict(set)
        
        for row in range(len(board)):
            current_row = set()
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue

                if board[row][col] in current_row:
                    return False
                current_row.add(board[row][col])

                if board[row][col] in col_mapping[col]:
                    return False
                col_mapping[col].add(board[row][col])

                box_i , box_j = row // 3 , col // 3
                if board[row][col] in box_mapping[(box_i , box_j)]:
                    return False
                box_mapping[(box_i , box_j)].add(board[row][col])
        
        return True
                
                