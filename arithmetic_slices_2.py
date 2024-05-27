# this question is on subsequences not subarrays
import collections
from typing import List

if __name__ == '__main__':
    a = {(1, 2): 100}
    x = a.get((0, 0), 0)
    print(x)


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        dp = collections.defaultdict(int)

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                cd = nums[i] - nums[j]
                dp[(i, cd)] += (1 + dp[(j, cd)])

        ans = 0
        for value in dp.values():
            ans += value

        # print(ans)

        n = len(nums)
        return ans - ((n * (n - 1)) // 2)
