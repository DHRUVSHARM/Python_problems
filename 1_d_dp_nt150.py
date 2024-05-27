# collection of 1d dp questions solved form nt 150
from typing import List

if __name__ == '__main__':
    a = {1, 2}
    b = a.copy()
    b.remove(2)
    print(a, b)
    c = "dhruv"
    print(c[-1: 100])
    d = {str(element) for element in range(1, 27)}
    print(d)
    c = "" + c
    print(list(c))
    print(len(""))

# climbing stairs
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(0, n + 1)]
        dp[0] = 1

        for index in range(1, n + 1):
            dp[index] = dp[index - 1]
            if index - 2 >= 0:
                dp[index] += dp[index - 2]

        return dp[n]
"""

# min cost to climb stairs
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is minimal cost to reach step i
        dp = [0 for _ in range(len(cost) + 1)]
        for index in range(2, len(cost) + 1):
            dp[index] = min(dp[index - 1] + cost[index - 1], dp[index - 2] + cost[index - 2])

        return dp[len(cost)]
"""

# house robber part 1
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(0, len(nums) + 1)]
        dp[0] = 0  # no houses to rob
        dp[1] = nums[0]  # no houses adjacent in the range [0..1]

        for index in range(2, len(nums) + 1):
            dp[index] = max(
                nums[index - 1] + dp[index - 2],  # include
                dp[index - 1]  # exclude
            )

        return dp[len(nums)]
"""

# house robber part 2
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def hrb(start, end) -> int:
            print(start , end)
            dp = {}
            for index in range(start, end + 1):
                dp[index - start] = max(
                    dp.get(index - start - 1 , 0),
                    dp.get(index - start - 2 , 0) + nums[index]
                )
            return dp[end - start]

        return nums[0] if len(nums) == 1 else max(hrb(0, len(nums) - 2), hrb(1, len(nums) - 1))
"""

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum % 2 != 0:
            return False

        exists, target = {0}, arr_sum // 2
        # the size of this set will never exceed sum(nums)

        # print(target)

        for element in nums:
            partial_sums = exists.copy()
            # print(partial_sums)
            for partial_sum in partial_sums:
                if partial_sum + element not in exists:
                    if partial_sum + element == target:
                        return True
                    exists.add(partial_sum + element)

        return False
"""

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for dp we need to get the maximal product subarray ending at index i
        # At least one size maximal product subarray is required
        res, max_prod, min_prod = float("-inf"), 1, 1
        for index in range(0, len(nums)):

            if nums[index] == 0:
                res = max(0 , res)
                max_prod, min_prod = 1, 1
                continue
            else:
                max_prod, min_prod = max(
                    nums[index] * max_prod,
                    nums[index] * min_prod,
                    nums[index]
                ), min(
                    nums[index] * max_prod,
                    nums[index] * min_prod,
                    nums[index]
                )

            res = max(res, max_prod)
        return res
"""

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # another interesting problem with 1d dp and python string slicing
        # handles all kinds of weird edge cases
        dp = [False for _ in range(0, len(s) + 1)]
        dp[-1] = True
        for index in range(len(dp) - 2, -1, -1):
            # print(index)
            for dictionary_word in wordDict:
                if index + len(dictionary_word) < len(dp):
                    # print(s[index: index + len(dictionary_word)])
                    dp[index] |= (
                            dictionary_word == s[index: index + len(dictionary_word)]
                            and dp[index + len(dictionary_word)]
                    )

        return dp[0]
"""

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = {str(element) for element in range(1, 27)}

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] in decodings else 0

        for index in range(2, len(s) + 1):
            dp[index] += dp[index - 1] if s[index - 1] in decodings else 0
            dp[index] += dp[index - 2] if s[index - 2] + s[index - 1] in decodings else 0

        # print(dp)

        return dp[len(s)]
"""

# interesting problem since it is substring we do not need extra dp memory
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd and even center
        res: str = ""

        def check(left, right):

            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1
            right -= 1

            if left <= right:
                # valid size palindrome
                if len(res) < right - left + 1:
                    res = s[left: right + 1]

        for index in range(len(s)):
            # odd center
            check(index, index)
            # even center
            check(index - 1, index)

        return res
"""

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        # odd and even center
        count: int = 0

        def check(left, right):

            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left += 1
            right -= 1

        for index in range(len(s)):
            # odd center
            check(index, index)
            # even center
            check(index - 1, index)

        return count
"""

# famous LIS length in O(nlogn) time complexity
# famous LIS length in O(nlogn) time complexity
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums
        dp = [0 for _ in range(0, len(nums))]
        min_frontier = [float("inf") for _ in range(0, len(nums))]
        min_frontier[0] = float("-inf")
        dp[0] = 0
        dp[1] = 1  # at least one size input
        min_frontier[1] = min(min_frontier[1], nums[1])

        def bin_search(left, right, element):
            while left + 1 < right:
                mid = left + int((right - left) / 2)
                if min_frontier[mid] < element:
                    left = mid
                else:
                    right = mid
            return left

        for index in range(2, len(nums)):
            jindex = bin_search(0, index, nums[index])
            dp[index] = jindex + 1
            min_frontier[jindex + 1] = min(min_frontier[jindex + 1], nums[index])

        # print(min_frontier)
        result = 0
        for element in dp:
            result = max(result, element)
        return result
"""


# the extremely famous coin change problem part 1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(0, amount + 1)]
        dp[0] = 0  # 0 coins is the minimum needed to get to 0

        for index in range(1, amount + 1):
            res = float("inf")
            for coin in coins:
                if index - coin >= 0:
                    if dp[index - coin] != -1:
                        res = min(res , dp[index - coin] + 1)

            dp[index] = -1 if res == float("inf") else res

        return dp[amount]
"""