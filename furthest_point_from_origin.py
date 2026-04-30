"""
Input: moves = "L_RL__R"
max right : 0
max left : -1
                    L   _ 

if l:
    ML = max left - 1 , recal

if r 
    mr = max right + 1 , recal

    update, maxl , maxr, and take max 

Output: 3
Explanation: The furthest point we can reach from the origin 0 is point -3 
through the following sequence of moves "LLRLLLR".

"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left , right = moves.count('L') , moves.count('R')
        return max(left , right) + (len(moves) - left - right) - min(left , right)