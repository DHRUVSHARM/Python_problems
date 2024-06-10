import collections
from typing import List

"""
print({"hello"})
a = [1, 2, 3]
print(a)
for element in a:
    element *= 2
print(a)
"""

# fun fact about the problem , in python , -ve numbers remainder is calculated like we did by adding mod to make
# positive

print(-2 % 5)
print(-22 % 5)
# gives 3 !!!


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for index in range(0, len(nums)):
            nums[index] = (nums[index] + (((abs(nums[index]) // k) * k) + k)) % k

        # print(nums)

        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]
            nums[index] %= k

        # print(nums)

        ans, p_sums = 0, collections.defaultdict(int)
        p_sums[0] = 1

        for element in nums:
            ans += p_sums[element]
            p_sums[element] += 1

        # print(p_sums)

        return ans
