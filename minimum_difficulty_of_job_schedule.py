from typing import List

if __name__ == "__main__":
    print(float("inf") + 1)


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # caching
        dp = {}

        def dfs(index, days, curr_max):

            if index == len(jobDifficulty):
                # we are choosing to have uncharted states
                if days == 0:
                    # valid selection
                    return 0
                else:
                    # invalid selection
                    return float("inf")
            elif days == 0:
                # the days are over before choosing everything , all of the jobs cannot be done
                return float("inf")

            curr_max = max(curr_max, jobDifficulty[index])
            if (index, days, curr_max) in dp:
                return dp[(index, days, curr_max)]

            result = float("inf")
            result = min(
                result,
                curr_max + dfs(index + 1, days - 1, float("-inf")),
                # consider this as the end
                dfs(index + 1, days, curr_max),
                # not consider as the end
            )

            dp[(index, days, curr_max)] = result
            return dp[(index, days, curr_max)]

        ans = dfs(0, d, float("-inf"))
        return -1 if ans == float("inf") else ans
