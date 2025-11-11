
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        dirs , guard_cell , wall_cell , guarded =[(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)] , set([(i , j) for i , j in guards]) , set([(i , j) for i , j in walls]) , set()

        def traverse(x , y):
            for dx , dy in dirs:
                # print("direction : " , dx , " " , dy)
                newx , newy = x + dx , y + dy
                while 0 <= newx < m and 0 <= newy < n and (newx , newy) not in wall_cell and (newx , newy) not in guard_cell :
                    # print("newx , newy : " , newx , " " , newy   )
                    if (newx, newy) not in guarded:
                        guarded.add((newx , newy))
                    newx , newy = newx + dx , newy + dy

        for i , j in guards:
            # print("guard : " , i , " " , j)
            traverse(i , j)

        return (m*n) - len(guarded) - len(guards) - len(walls)
    