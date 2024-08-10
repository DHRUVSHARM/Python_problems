class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        rows , cols = 4 * n , 4 * n

        changed_grid = [[0 for _ in range(cols)] for _ in range(rows)]

        # these are the three cases
        cases = {
            '/' : [(0 , 3) , (1 , 2) , (2 , 1) , (3 , 0)],
            '\\' : [(0 , 0) , (1 , 1) , (2 , 2) , (3 , 3)],
            ' ' : []
        }

        ans = 0
        x , y = 0 , 0


        for i in range(0 , len(grid)):
            for j in range(0 , len(grid[i])):
                # print("x : " , x , " , " , "y : " , y)
                print(grid[i][j] , end = " ")
                
                # check for the correct case
                if grid[i][j] == " ":
                    pass
                elif grid[i][j] == '/':
                    for dx , dy in cases[grid[i][j]]:
                        changed_grid[x + dx][y + dy] = 1
                else:
                    for dx , dy in cases['\\']:
                        changed_grid[x + dx][y + dy] = 1
                       

                # print("original : x , y : " , x , " , " , y)
                y = (y + 4) % (cols)
                # print("new : x , y : " , x , " , " , y)
            print("")

            x  = (x  + 4) % (rows)
        

        print("created grid ")

        for i in range(0 , rows):
            for j in range(0 , cols):
                print(changed_grid[i][j] , end = " ")
            print("")

        print("created grid ")

        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        visited = set()
        
        def dfs(i , j):
            visited.add((i , j))
            
            for di , dj in directions:
                newi , newj = i + di , j + dj
                if 0 <= newi < rows and 0 <= newj < cols and (newi , newj) not in visited and changed_grid[newi][newj] == 0:
                    dfs(newi , newj) 

        
        for i in range(rows):
            for j in range(cols):
                if (i , j) not in visited and changed_grid[i][j] == 0:
                    ans += 1
                    dfs(i , j)

        return ans