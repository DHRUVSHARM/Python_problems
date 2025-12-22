from typing import List 

class Solution:
    
    def debug_arr(arr):
        m , n = len(arr) , len(arr[0])

        for i in range(0 , m):
            print("/n")
            for j in range(0 , n):
                print(arr[i][j] , " ")
    
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff , res = [[0 for _ in range(0 , n + 1)] for _ in range(0 , n + 1)] , [[0 for _ in range(0 , n)] for _ in range(0 , n)]
        
        for si , sj , ei , ej in queries:
            diff[si][sj] += 1
            diff[si][ej + 1] -= 1
            diff[ei + 1][sj] -= 1
            diff[ei + 1][ej + 1] += 1

        # row wise iteration
        for i in range(0 , n):
            for j in range(0 , n):
                if j == 0:
                    res[i][j] += diff[i][j]
                else:
                    res[i][j] += (res[i][j-1] + diff[i][j])

        # col wise iteration
        for j in range(0 , n):
            for i in range(0 , n):
                if i == 0:
                    pass
                else:
                    res[i][j] += res[i-1][j]

            
        return res
