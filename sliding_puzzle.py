import collections
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # (steps , (i , j) , (1 , 2 , 3 , 4 , 5 , 0))
        seen , nodes , m , n = set() , collections.deque() , len(board) , len(board[0])

        zero_index , target = () , (1 , 2 , 3 , 4 , 5 , 0)

        for i in range(0 , m):
            for j in range(0 , n):
                if board[i][j] == 0:
                    zero_index = (i , j)
                    break
        
        nodes.append((
                       zero_index,
                         (
                             board[0][0],
                             board[0][1],
                             board[0][2],
                             board[1][0],
                             board[1][1],
                             board[1][2]
                             )))
        
        solved , level , seen , directions = False , 0 , set([    (
                             board[0][0],
                             board[0][1],
                             board[0][2],
                             board[1][0],
                             board[1][1],
                             board[1][2]
                             ) ]) , [(-1 , 0) , (1 , 0) , (0 , 1) , (0 , -1)]
        
        while nodes:
            
            level_size = len(nodes)
            
            while level_size:
                
                current_index , state = nodes.popleft()
                if state == target:
                    return level
                
                for dx , dy in directions:
                    newx , newy = current_index[0] + dx , current_index[1] + dy
                    if 0 <= newx < m and 0 <= newy < n:
                        new_state = [element for element in state]
                        new_state[3*current_index[0] + current_index[1]] , new_state[3*newx + newy] = new_state[3*newx + newy] , new_state[3*current_index[0] + current_index[1]] 
                        new_state = tuple(new_state)
                        if new_state not in seen:
                            seen.add(new_state)
                            nodes.append(( (newx , newy) , new_state ))
                
                level_size -= 1

            level += 1

        return -1