import math

if __name__ == '__main__':
    pass

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # matrix is of n * n
        arr = [[1 for _ in range(0, n)] for _ in range(0, n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        root = 1
        # all matrices break down to size 1 or 2
        while True:

            if r - l + 1 == 1:
                arr[t][l] = root
                break

            if r - l + 1 == 2:
                arr[t][l] = root
                root += 1
                arr[t][r] = root
                root += 1
                arr[b][r] = root
                root += 1
                arr[b][l] = root
                break

            row = l
            for col in range(l, r + 1):
                arr[row][col] = root
                root += 1
            t += 1
            col = r
            for row in range(t, b + 1):
                arr[row][col] = root
                root += 1
            r -= 1
            row = b
            for col in range(r, l - 1, -1):
                arr[row][col] = root
                root += 1
            b -= 1
            col = l
            for row in range(b, t - 1, -1):
                arr[row][col] = root
                root += 1
            l += 1

        return arr
