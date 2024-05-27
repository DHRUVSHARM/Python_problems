from typing import List, Optional

if __name__ == '__main__':
    for z in range(0, 5):
        l, r = 1, 1 + z
        while r < 5 + 1:
            # if l == r:
            # print("check !!!")
            # continue
            print("l , r : ", l, r)
            l += 1
            r += 1
        print(True ^ False)
# unique bsts part 1
"""
class Solution:
    def numTrees(self, n: int) -> int:
        # interval style important dp question about bsts
        dp = [ [0 for _ in range(0, n + 1)] for _ in range(0, n + 1) ]
        # print(n)
        for z in range(0, n):
            l, r = 1, 1 + z
            while r < n + 1:
                if l == r:
                    # print("l , r ",  l , r)
                    dp[l][r] = 1
                elif l < r:
                    # we will have to count with different roots
                    res = 0
                    for mid in range(l, r + 1):
                        res += (dp[mid + 1][r] if mid + 1 <= r else 1) * \
                               (dp[l][mid - 1] if mid - 1 >= l else 1)
                    dp[l][r] = res

                l += 1
                r += 1

        return dp[1][n]
"""

# unique bsts part 2
# Definition for a binary tree node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

        def build(l, r, mid, left, right):
            # we will have to count with different roots
            for l_node in left:
                for r_node in right:
                    middle_node = TreeNode(mid)
                    middle_node.left = l_node
                    middle_node.right = r_node
                    dp[l][r].append(middle_node)

        for z in range(0, n):
            l, r = 1, 1 + z
            while r < n + 1:

                if l == r:
                    # only one tree can be created
                    dp[l][r] = [TreeNode(l)]
                elif l > r:
                    # invalid stuff
                    pass
                else:
                    # we need to build the tree
                    for mid in range(l, r + 1):
                        right = dp[mid + 1][r] if mid + 1 <= r else [None]
                        left = dp[l][mid - 1] if mid - 1 >= l else [None]
                        build(l, r, mid, left, right)

                l += 1
                r += 1

        return dp[1][n]
"""

# longest common palindromic subsequence
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for z in range(0, n):
            l, r = 1, 1 + z
            while r < n + 1:

                if l == r:
                    # base case
                    dp[l][r] = 1
                    # 1 sized palindromic subsequence
                else:
                    if s[l - 1] == s[r - 1]:
                        dp[l][r] = 2 + dp[l + 1][r - 1]
                    else:
                        dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

                l += 1
                r += 1

        return dp[1][n]
"""

# longest common subsequence
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(0, m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

        return dp[m][n]
"""

# coin change 2
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # sorting does not matter ,but if you want you can terminate early
        coins.sort()
        dp = [[0 for _ in range(0, amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(0, len(coins) + 1):
            # 1 way to make 0 amount
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # we try to use as much of the coin denomination
                    dp[i][j] += dp[i][j - coins[i - 1]]
                # we ignore this denomination and use smaller ones
                dp[i][j] += dp[i - 1][j]

        return dp[len(coins)][amount]
"""

# unique paths part 2
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(0, n)] for _ in range(0, m)]

        dp[0][0] = 0 if obstacleGrid[0][0] else 1

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if not obstacleGrid[i][0] else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if not obstacleGrid[0][j] else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
"""

# ******************************************
# some 0/1 knapsack problems
# target sums using signs + and -
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        # we will try bottom up dp
        cum_sum = sum(nums)
        for total in range(-cum_sum, +cum_sum + 1):
            dp[(0, total)] = 1 if total == 0 else 0

        # now we build
        for i in range(1, len(nums) + 1):
            for total in range(-cum_sum, cum_sum + 1):
                dp[(i, total)] = dp.get((i - 1, total - nums[i - 1]), 0) + \
                                 dp.get((i - 1, total + nums[i - 1]), 0)

        return dp.get((len(nums), target), 0)
"""

# another interesting 3d knapsack problem , again i do a bottom up interesting solution
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[[0 for _ in range(0, n + 1)] for _ in range(0, m + 1)] for _ in range(0, len(strs) + 1)]
        zero_count = {}
        for s in strs:
            res = 0
            for element in s:
                if element == "0":
                    res += 1
            zero_count[s] = (res , len(s) - res)

        for index in range(1, len(strs) + 1):
            for max_zeroes in range(0, m + 1):
                for max_ones in range(0, n + 1):
                    result = 0
                    zeroes, ones = zero_count[strs[index - 1]]
                    if max_zeroes - zeroes >= 0 and max_ones - ones >= 0:
                        # can include
                        result = max(result, 1 + dp[index - 1][max_zeroes - zeroes][max_ones - ones])
                    # can exclude
                    result = max(result, dp[index - 1][max_zeroes][max_ones])
                    dp[index][max_zeroes][max_ones] = result

        return dp[len(strs)][m][n]
"""

# another 0/1 knapsack reducible problem
# greedy will not work
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        pile_target = stone_sum // 2
        dp = [[0 for _ in range(0, pile_target + 1)] for _ in range(0, len(stones) + 1)]
        # dp[index][pile_limit] = maximal stone sum available with pile_limit and 1..index stones
        # available

        for index in range(1, len(stones) + 1):
            for pile_limit in range(1, pile_target + 1):
                res = 0
                # exclude the stone
                res = max(res, dp[index - 1][pile_limit])
                if pile_limit - stones[index - 1] >= 0:
                    res = max(res, stones[index - 1] + dp[index - 1][pile_limit - stones[index - 1]])

                dp[index][pile_limit] = res

        return abs(dp[len(stones)][pile_target] - (stone_sum - dp[len(stones)][pile_target]))
"""

# ************************************************

# an unbounded knapsack problem
# minimum cost for tickets
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # top down is better for this problem
        dp = {}

        def find(element):
            ans = -1
            for index in range(0, len(days)):
                if days[index] >= element:
                    ans = index
                    break
            # print("ans : " , ans , element)
            return days[-1] + 1 if ans == -1 else days[ans]

        def dfs(day) -> int:
            if day in dp:
                return dp[day]

            if day > days[-1]:
                # we have completed the task
                return 0

            # we will try using the passes 1 , 7 , and 30 at every point
            res = float("inf")
            # but we will need to find the correct day
            res = min(
                res,
                costs[0] + dfs(find(day + 1)),
                costs[1] + dfs(find(day + 7)),
                costs[2] + dfs(find(day + 30)),

            )

            dp[day] = res
            return dp[day]

        return dfs(days[0])
"""

# ************************************************

# lcs based problems
# distinct subsequences
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(0, len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] += dp[i - 1][j]

        return dp[len(s)][len(t)]
"""

# edit distance
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(0, len(word2) + 1)] for _ in range(0, len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = 1 + dp[i - 1][0]
        for j in range(1, len(word2) + 1):
            dp[0][j] = 1 + dp[0][j - 1]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    # it is always better to match and shorten the problem for
                    # free
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = min(
                        1 + dp[i - 1][j],
                        1 + dp[i][j - 1],
                        1 + dp[i - 1][j - 1]
                    )

        return dp[len(word1)][len(word2)]
"""

# this version passes all testcases but MLE
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            dp[i][0] = dp[i - 1][0] + str1[i - 1]
        for j in range(1, len(str2) + 1):
            dp[0][j] = dp[0][j - 1] + str2[j - 1]

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i][j-1]) <= len(dp[i-1][j]):
                        dp[i][j] = dp[i][j - 1] + str2[j-1]
                    else:
                        dp[i][j] = dp[i-1][j] + str1[i-1]

        return dp[len(str1)][len(str2)]
"""

"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        result = ""

        for i in range(1, len(str1) + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, len(str2) + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        # tracing
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            # print(i , j)
            if str1[i - 1] == str2[j - 1]:
                result = str1[i - 1] + result
                i -= 1
                j -= 1
            else:
                if dp[i][j - 1] <= dp[i - 1][j]:
                    result = str2[j - 1] + result
                    j -= 1
                else:
                    result = str1[i - 1] + result
                    i -= 1
            # print("result : " , result , len(result))
        while i > 0:
            result = str1[i - 1] + result
            i -= 1
        while j > 0:
            result = str2[j - 1] + result
            j -= 1

        return result
"""

# interesting problem where 3d - 2d then to 1d in terms of memory
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(0, len(s2) + 1)] for _ in range(0, len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and (s3[i - 1] == s1[i - 1])
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and (s3[j - 1] == s2[j - 1])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = dp[i][j] or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]) \
                           or (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j])

        return dp[len(s1)][len(s2)]
"""

# memory 1d
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False for _ in range(0, len(s2) + 1)]
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = (s3[j - 1] == s2[j - 1]) and dp[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                res = False
                res = res or (s3[i + j - 1] == s1[i - 1] and dp[j])
                if j > 0:
                    res = res or (s3[i + j - 1] == s2[j - 1] and dp[j - 1])

                dp[j] = res

        return dp[len(s2)]
"""

# so in my solution , the dp requires 3 variables,  since you are breaking the problem
# that way, if you want to reduce it to 2 variables only , then we must make the dfs function free
# from the 3 variables, realize that a cost for buying will have to be subtracted from profit
# no matter what,
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        print(prices)

        def dfs(index, bought, buying_price) -> int:

            if (index, bought, buying_price) in dp:
                return dp[(index, bought, buying_price)]

            if index >= len(prices):
                # out of bounds , nothing can be done
                return 0

            res = 0
            if bought:
                # selling and ignoring are the options
                res = max(
                    res,
                    prices[index] - buying_price + dfs(index + 1 + 1, bought ^ True, -1),
                    dfs(index + 1, bought, buying_price)
                )
            else:
                # buying and ignoring are the options
                res = max(
                    res,
                    dfs(index + 1, bought ^ True, prices[index]),
                    dfs(index + 1, bought, buying_price)
                )

            dp[(index, bought, buying_price)] = res
            return res

        return dfs(0, False, -1)
"""

"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # every
        m, n = len(matrix), len(matrix[0])
        # print("m , n: ",  m , n)
        dp = {}
        # directions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        
        def dfs(i, j) -> int:
            
            lip from the start point i , j
            :param i:
            :param j:
            :return:
            
            if (i, j) in dp:
                return dp[(i, j)]

            if not (0 <= i <= m - 1 and 0 <= j <= n - 1):
                # out of range position
                return 0

            res = 1
            # print("i , j : " , i , j)
            # at least one size max path
            for direction in directions:
                dx, dy = direction
                newx, newy = i + dx, j + dy
                # print("new : " , newx , newy)
                if 0 <= newx <= m - 1 and 0 <= newy <= n - 1 and matrix[i][j] < matrix[newx][newy]:
                    res = max(
                        res,
                        1 + dfs(newx, newy)
                    )

            dp[(i, j)] = res
            return res
        
        ans = 0
        for i in range(0 , m):
            for j in range(0 , n):
                if (i , j) not in dp:
                    ans = max(ans , dfs(i , j))

        return ans
"""

# this is one of the daily's, so I added it,
# but we need cn optimize it to an O(1) solution
"""
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [[False for _ in range(0, len(nums) + 1)] for _ in range(0, len(nums) + 1)]

        for z in range(0, len(nums) + 1):
            l, r = 0, 0 + z
            while r < len(nums) + 1:
                if r == l:
                    pass
                if r - l + 1 == 2:
                    if nums[l - 1] == nums[r - 1]:
                        dp[l][r] = True
                elif r - l + 1 == 3:
                    if nums[l - 1] == nums[l] and nums[l] == nums[r - 1]:
                        dp[l][r] = True
                    elif nums[l] - nums[l - 1] == 1 and nums[r - 1] - nums[l] == 1:
                        dp[l][r] = True
                else:
                    for k in range(l, r):
                        dp[l][r] = dp[l][r] or (
                                dp[l][k] and dp[k + 1][r]
                        )

                r += 1
                l += 1

        return dp[1][len(nums)]
"""

# linear time optimized final solution
"""
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False for _ in range(0, len(nums) + 1)]
        dp[0] = True
        for index in range(2, len(nums) + 1):
            dp[index] = dp[index] or (
                    (nums[index - 1] == nums[index - 2]) and dp[index - 2]
                    or (
                        False if index == 2 else (
                                (nums[index - 1] == nums[index - 2] and nums[index - 2] == nums[index - 3]
                                 or nums[index - 1] - nums[index - 2] == 1 and nums[index - 2] - nums[index - 3] == 1)
                                and dp[index - 3]
                        )
                    )
            )

        return dp[len(nums)]
"""

# another top down dp solution
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(left, start, end, right) -> int:

            if (start, end) in dp:
                return dp[(start, end)]

            if start > end:
                return 0

            if start == end:
                return left * nums[start] * right

            res = 0
            for k in range(start, end + 1):
                res = max(
                    res,
                    dfs(left, start, k - 1, nums[k])
                    + (left * right * nums[k])
                    + dfs(nums[k], k + 1, end, right)
                )

            dp[(start, end)] = res
            return res

        return dfs(1, 0, len(nums) - 1, 1)
"""


# another top down dp solutions
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(s_index, p_index) -> bool:
            if (s_index, p_index) in dp:
                return dp[(s_index, p_index)]

            if s_index == len(s) and p_index == len(p):
                return True
            if s_index < len(s) and p_index == len(p):
                # string still left to match
                return False

            res = False

            # print("p_index , s_index : " , p_index , s_index)

            if p_index + 1 < len(p) and p[p_index + 1] == "*":
                # start operation
                # print("p_index , s_index : " , p_index , s_index)
                if s_index < len(s):
                    # can reduce
                    if p[p_index] == "." or p[p_index] == s[s_index]:
                        res = res or dfs(s_index + 1, p_index)
                # can stop the production
                res = res or dfs(s_index, p_index + 2)

            else:
                # one sized operation
                if s_index < len(s):
                    if p[p_index] == ".":
                        res = res or dfs(s_index + 1, p_index + 1)
                    else:
                        res = res or (False if s[s_index] != p[p_index] else dfs(s_index + 1, p_index + 1))

            dp[(s_index, p_index)] = res
            return res

        return dfs(0, 0)
"""