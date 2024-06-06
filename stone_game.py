from typing import List

if __name__ == "__main__":
    pass


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # first problem in the series
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for r in range(0, n):
            for l in range(0, n):
                if r < l:
                    # invalid interval
                    continue
                elif r == l:
                    # base always a Bob - Alice situation since number of piles is even
                    dp[r][l] = piles[l]
                else:
                    # checking max in both cases because of interesting mini - max algo
                    dp[r][l] = max(piles[r] - dp[r - 1][l], piles[l] - dp[r][l + 1])

        return True if dp[n - 1][0] > 0 else False
