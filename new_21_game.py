if __name__ == "__main__":
    for i in range(3, -1, -1):
        print(i)


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        dp = {}

        # print("n ,k max : " , n , k , maxPts)
        # here the state is going to be tracked by the points accumulated
        def dfs(points: float) -> float:

            if points in dp:
                return dp[points]

            if points >= k:
                dp[points] = 1
                return dp[points]

            dp[points] = 0
            for draw in range(1, maxPts + 1):
                newPoints = points + draw
                if newPoints <= n:
                    dp[points] += dfs(newPoints)
            dp[points] /= maxPts

            return dp[points]

        return dfs(0)
        """

        dp = [0 for _ in range(k + maxPts + 1)]

        window_sum, l, r = 0, k, k + maxPts

        for index in range(k, k + maxPts + 1):
            if index <= n:
                dp[index] = 1
                # can get point in this range
            window_sum += dp[index]

        window_sum -= dp[r]
        r -= 1

        for i in range(k - 1, -1, -1):
            # print("window size : ", i, r, i)
            dp[i] = window_sum / maxPts
            window_sum += dp[i] - dp[r]
            r -= 1

        return dp[0]
