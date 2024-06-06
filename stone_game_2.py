from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # second problem in the series
        n = len(piles)
        total = 0
        for element in piles:
            total += element
        # cache
        dp = {}

        def dfs(l: int, r: int, m: int, player: int) -> int:
            """
            here the state is a range of the piles array , we also need to keep
            track of M also , so this style is best
            :param player: 0 for alice , 1 for bob
            :param m: M
            :param l: start pt
            :param r: end pt
            :return: result
            """

            if (l, r, m, player) in dp:
                return dp[(l, r, m, player)]

            if l > r:
                return 0

            dp[(l, r, m, player)] = float("-inf")
            sum = 0

            for x in range(1, 2 * m + 1):

                if l + x - 1 > r:
                    continue

                sum += piles[l + x - 1]

                dp[(l, r, m, player)] = max(
                    dp[(l, r, m, player)], sum - dfs(l + x, r, max(m, x), player ^ 1)
                )

            return dp[(l, r, m, player)]

        ans = dfs(0, n - 1, 1, 0) + total
        return ans // 2
