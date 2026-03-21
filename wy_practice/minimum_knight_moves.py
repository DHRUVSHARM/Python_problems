"""
Docstring for wy_practice.minimum_knight_moves

    r

  r   0 ,0  r

r
  r


  circular ring that moves outward combines target
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
  

0 0 0
0 0 0 
0 0 0
"""

# possible solution meet in the middle as well

import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs , visited , q = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)] , set([(0 ,0)]) , collections.deque([(0 , 0)])

        result = 0


        x , y = abs(x) , abs(y) # symmetric reduction
        while q:
            level_size = len(q)
            while level_size:
                nx , ny  = q.popleft()

                if nx == x and ny == y:
                    return result

                # will push the reachable children into the queue
                for dx , dy in dirs:
                    newx , newy = nx + dx , ny + dy
                    # there are no ranges here  
                    if -2 <= newx < x + 3 and -2 <= newy < y + 3 and (newx , newy) not in visited:
                        q.append((newx , newy))
                        visited.add((newx , newy))


                level_size -= 1

            # next level 
            result += 1
        
        return result