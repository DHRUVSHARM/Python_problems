import collections
from typing import List

if __name__ == "__main__":
    a = collections.defaultdict(int)
    print(a["1"])
    print(a[0])
    a["a"] = 100
    print(a.get("a", -1))


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = collections.defaultdict(int)
        for index in range(0, len(arr)):
            dp[index] = 0

        for index in range(0, len(arr)):
            max_element = arr[index]
            for j in range(0, k):
                if index - j >= 0:
                    max_element = max(max_element, arr[index - j])
                    dp[index] = max(
                        dp[index], dp[index - j - 1] + max_element * (j + 1)
                    )

        return dp[len(arr) - 1]
