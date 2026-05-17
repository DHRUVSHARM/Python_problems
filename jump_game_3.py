from typing import List

import collections
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs ? since we can find the next states possible, from the current node
        # no need to revisit ? since when we push one of the indices in the 
        # visited we have already considered the path 
        # 0 is like a dead node, we cannot move from it 
        n = len(arr)
        q = collections.deque([(start , arr[start])])
        visited = set()

        while len(q):
            index, val = q.popleft()
            if val == 0:
                return True
            
            if 0 <= (index + val) < n and (index + val) not in visited:
                visited.add((index + val))
                q.append((index + val, arr[index + val]))

            if 0 <= (index - val) < n and (index - val) not in visited:
                visited.add(index - val)
                q.append((index - val, arr[index - val]))

        return False