"""
There is a robot starting at the position (0, 0), the origin, 
on a 2D plane. Given a sequence of its moves, 
judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence 
of the robot where moves[i] represents its ith move. 
Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 
'R' will always make the robot move to the right once, 'L' 
will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.


1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {
            'U' : (-1 , 0),
            'D' : (1 , 0),
            'L' : (0 , -1),
            'R' : (0 , 1) 
        }
        
        x , y = 0 , 0
        for move in moves:
            dx , dy = move_map[move]
            x , y = x + dx , y + dy


        return x == 0 and y == 0