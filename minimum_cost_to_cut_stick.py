from typing import List

if __name__ == "__main__":
    n = 7
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    value = 1
    z = 0
    while z <= n:
        i, j = z, 0
        while i <= n:
            dp[i][j] = value
            value += 1
            i += 1
            j += 1
        z += 1

    for row in dp:
        print(row)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        length = len(cuts) + 2
        dp = [[0 for _ in range(length)] for _ in range(length)]
        cuts.sort()
        cuts = [0] + cuts + [n]
        # this the best iterative solution as we are not considering unwanted l , r intervals
        z = 0
        while z < length:
            r, l = z, 0
            while r < length:
                # print("r , l " , r , l)
                if r - l <= 1:
                    dp[r][l] = 0
                else:
                    res = float("inf")
                    for k in range(l + 1, r):
                        res = min(res, cuts[r] - cuts[l] + dp[k][l] + dp[r][k])
                    # note that we will always have an answer
                    dp[r][l] = res
                r += 1
                l += 1
            z += 1
        return dp[length - 1][0]


"""
# we will solve this using the dp iterative style
# note that each cut can be used only once
# we will solve this using the dp iterative style
# note that each cut can be used only once
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        count = 0
        z = 0
        while z <= n:
            r, l = z, 0
            while r <= n:
                if r - l <= 1:
                    dp[(r , l)] = 0
                else:
                    res = float('inf')
                    for c in cuts:
                        if l < c < r:
                            res = min(res, r - l + dp[(c , l)] + dp[(r , c)])
                    dp[(r , l)] = 0 if res == float('inf') else res
                count += 1
                l += 1
                r += 1
            z += 1

        print(count)
        return dp[(n , 0)]
"""
"""
# we will solve this problem using both memoization and the dp iterative style
# note that each cut can be used only once
class Solution:
    def minCostMemoized(self, n: int, cuts: List[int]) -> int:
        dp = {}

        # this represents the state transition
        def dfs(l: int, r: int) -> int:

            if (l, r) in dp:
                return dp[(l, r)]

            if r - l == 1:
                dp[(l, r)] = 0
                return dp[(l, r)]

            res = float('inf')

            for c in cuts:
                if l < c < r:
                    # possible cut
                    res = min(res, r - l + dfs(l, c) + dfs(c, r))

            dp[(l, r)] = 0 if res == float('inf') else res

            return dp[(l, r)]

        return dfs(0, n)
"""
