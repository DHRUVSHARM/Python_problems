from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # note m is vertical and for rows and n is horizontal for columns
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = (0, 0)
        """
        for row in dp:
            print(row)
        print("\n")
        """
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue

                l, r = 0, 0
                if i - 1 >= 0 and j - 1 >= 0:
                    l = dp[i - 1][j - 1][0]
                    r = dp[i - 1][j - 1][1]
                if i - 1 >= 0:
                    l = min(dp[i - 1][j][0], l)
                    r = min(dp[i - 1][j][1], r)
                if j - 1 >= 0:
                    l = min(dp[i][j - 1][0], l)
                    r = min(dp[i][j - 1][1], r)

                dp[i][j] = (1 + l, 1 + r)
                ans = max(ans, ((1 + r) * (1 + l)))

        """
        for row in dp:
            print(row)
        print("\n")
        """
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    ))
