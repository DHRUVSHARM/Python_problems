from typing import List


# interesting dp with cumulative sums
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # to store the subproblems
        dp = {}

        def dfs(index, remaining_jobs) -> int:
            """
            returns the minimal cost to complete all jobs with [index:] and remaining jobs as as
            remaining
            :param index: current index of jobs considered by the paid painter
            :param remaining_jobs: remaining jobs left considering the the free painter
            tries to do the remaining jobs when the paid painter is free
            :return: the minimal cost
            """

            if (index, remaining_jobs) in dp:
                return dp[(index, remaining_jobs)]

            # base cases
            if remaining_jobs <= 0:
                # all done no cost
                return 0

            if index == len(cost):
                # we are here and a remaining job is still left , not possible
                return (10 ** 6) * 500 * 10

            result = min(
                cost[index] + dfs(index + 1, remaining_jobs - 1 - time[index]),
                dfs(index + 1, remaining_jobs)
            )

            dp[(index, remaining_jobs)] = result
            return result

        return dfs(0, len(cost))
