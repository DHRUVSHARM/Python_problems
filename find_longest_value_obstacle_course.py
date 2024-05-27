import bisect
from typing import List

if __name__ == '__main__':
    # 2-D lists
    arr = [[0] * 4 for i in range(4)]
    print(arr)
    print(arr[0][0], arr[3][3])

    # This won't work as you expect it to
    arr = [[0] * 4] * 4
    arr[0][0] = 1
    print(arr)

    # bisect method helps in upper and lower bound
    arr = [0, float('inf')]
    index = bisect.bisect(arr, 10)
    print("index : ", index)


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # simple lis type solution , o(n^2)
        """
        ans = [0 for _ in range(0, len(obstacles))]
        for i, element in enumerate(obstacles):
            j = i - 1
            # finding the maximal increasing sequence to attach to
            while j >= 0:
                if obstacles[j] <= element:
                    ans[i] = max(ans[i], ans[j])
                j -= 1
            # attaching your own self
            ans[i] += 1
        print("ans : ", ans)
        return ans
        """
        # optimized solution  , o(nlogn)
        # for simplicity base case
        obstacle_lis = [0 for _ in range(0, len(obstacles))]  # keeps track of the answer
        dp = [float('inf') for _ in range(0, len(obstacles) + 1)]
        # keeps track of the smallest frontier for each length
        dp[0] = 0  # for handling edge cases

        for i, element in enumerate(obstacles):
            index = bisect.bisect(dp, element)
            obstacle_lis[i] = index
            dp[index] = min(dp[index], element)

        print("dp : ", dp)
        return obstacle_lis
