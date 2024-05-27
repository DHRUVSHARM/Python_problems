from typing import List

if __name__ == '__main__':
    pass


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        root = 1
        ans = []

        while l < r and t < b:
            for col in range(l, r + 1):
                ans.append(matrix[t][col])
                root += 1
            t += 1
            for row in range(t, b + 1):
                ans.append(matrix[row][r])
                root += 1
            r -= 1
            for col in range(r, l - 1, -1):
                ans.append(matrix[b][col])
                root += 1
            b -= 1
            for row in range(b, t - 1, -1):
                ans.append(matrix[row][l])
                root += 1
            l += 1
            print("ans : ", ans)

        if l == r and t == b:
            ans.append(matrix[l][r])
        elif t == b:
            for col in range(l, r + 1):
                ans.append(matrix[t][col])
                root += 1
        elif l == r:
            for row in range(t, b + 1):
                ans.append(matrix[row][l])
                root += 1

        return ans
