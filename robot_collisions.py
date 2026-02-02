from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [(pos , health, direction) for pos, health, direction in zip(positions , healths , directions)]
        robots.sort()

        s = []

        for pos, health, direction in robots:
            
            exploded = False
            while not exploded and s and s[-1][2] == "R" and direction == "L":
                # collision expected
                if s[-1][1] < health:
                    # remove from the stack, continue , decrease health of hitter
                    health -= 1
                    s.pop()
                elif s[-1][1] == health:
                    # both removed and stop
                    exploded = True 
                    s.pop()
                else:
                    # the hitter is destroyed , but the frontier health is reduced
                    exploded = True
                    p , h , d = s.pop()
                    h -= 1
                    s.append((p , h , d))
            # s empty, collisions are complete, or we can say the same directions, or L and R (never collide)
            if not exploded:
                s.append((pos , health , direction))

        health_mapping , result = {pos : health for pos, health, _ in s} , []
        for pos in positions:
            if pos in health_mapping:
                result.append(health_mapping[pos])
        
        return result