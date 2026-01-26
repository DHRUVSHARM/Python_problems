from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for element in asteroids:
            collapsed = False
            if element < 0:
                while s and s[-1] > 0:
                    if s[-1] > abs(element):
                        collapsed = True
                        break
                    elif s[-1] == abs(element):
                        # print("both blast : " , s[-1] , " " , element)
                        s.pop()
                        collapsed = True
                        break
                    else:
                        s.pop()
                if not collapsed:
                    s.append(element)
            else:
                # a positive element can be added 
                # but we maintain positive , or negatives
                # if positive then simple add
                # if negative at top then all behind is also negative, so diff direction so does not matter anyway
                s.append(element)
        
        return s