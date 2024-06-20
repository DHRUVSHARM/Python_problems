import collections
from typing import List


arr = ["a", "b", "c"]
arr_set = set(arr)

print(arr_set)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = collections.defaultdict(list)

        # backtrack dfs with memoization for some cases
        def dfs(index):
            print("index : ", index)
            if index == len(s):
                return [""]

            if index in memo:
                return memo[index]

            res = []
            prefix = []

            for i in range(index, len(s)):
                prefix.append(s[i])
                curr = "".join(prefix)

                if curr in wordDict:
                    curr_result = []
                    sub_result = dfs(i + 1)
                    for sr in sub_result:
                        curr_result.append(curr + " " + sr)
                    res.extend(curr_result)

            memo[index] = res
            return res

        result = dfs(0)
        for index in range(0, len(result)):
            result[index] = result[index].strip()

        return result
