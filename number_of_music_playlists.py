class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # interesting and difficult permutation style problem
        dp = {}

        def dfs(current_goal, old_songs) -> int:

            if (current_goal, old_songs) in dp:
                return dp[(current_goal, old_songs)]

            if current_goal == 0:
                if old_songs == n:
                    # we have used n songs at least one
                    return 1
                else:
                    # invalid situation
                    return 0

            res = 0
            # 2 ways to fill the first position
            # using a new song
            res += (n - old_songs) * dfs(current_goal - 1, old_songs + 1)
            # using a old song , if the waiting period is over
            res += 0 if (old_songs - k <= 0) else (old_songs - k) * dfs(current_goal - 1, old_songs)

            dp[(current_goal, old_songs)] = res
            return res

        return dfs(goal, 0) % (10 ** 9 + 7)
