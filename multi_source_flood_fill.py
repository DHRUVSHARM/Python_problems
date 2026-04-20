"""
n , m : rows, cols 


[[1,0,0],
[[0,0,0],
[[0,0,2],


[[1,1,1],
[1,1,2],
[1,2,2]]

Expected

[[1,1,2],
[1,2,2],
[2,2,2]]

"""
import collections
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # multi src bfs
        sources.sort(key = lambda element : -1*element[2])
        # print(sources)
        q = collections.deque(sources)
        dirs = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]
        grid = [[0 for _ in range(m)] for _ in range(n)]

        for r,c,color in q:
            grid[r][c] = color

        while len(q):
            r , c , color = q.popleft()
            for dr , dc in dirs:
                newr, newc = r + dr , c + dc
                if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 0:
                    grid[newr][newc] = color
                    q.append([newr , newc , color])
        
        return grid