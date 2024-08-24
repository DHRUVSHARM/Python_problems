class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        ans = float("-inf")

        for row in range(1, m):
            left = [0 for _ in range(0, n)]
            right = [0 for _ in range(0, n)]

            for col in range(0, n):
                left[col] = points[row - 1][col]
                if col - 1 >= 0:
                    left[col] = max(left[col], left[col - 1] - 1)

            for col in range(n - 1, -1, -1):
                right[col] = points[row - 1][col]
                if col + 1 < n:
                    right[col] = max(right[col], right[col + 1] - 1)

            for col in range(0, n):
                points[row][col] += max(left[col], right[col])

        for col in range(0, n):
            ans = max(ans, points[-1][col])

        return ans
