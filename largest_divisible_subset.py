from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # the smallest will be of size 1
        ls = {i: [nums[i]] for i in range(len(nums))}
        # ending here the best subset is the single element only

        for i in range(1, len(nums)):
            index = -1
            for j in range(i - 1, - 1, -1):
                if nums[i] % nums[j] == 0:
                    if 1 + len(ls[j]) > len(ls[i]):
                        index = j
            if index != -1:
                ls[i] = ls[index] + [nums[i]]

        # print(ls)

        ans = []
        for key, value in ls.items():
            if len(value) > len(ans):
                ans = value

        return ans
