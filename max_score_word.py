import collections
from typing import List

a = {"a": 3}
b = a.copy()
b["a"] -= 1
print(a)
print(b)

print(ord("a"))


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        freq = {i: 0 for i in range(26)}
        for ele in letters:
            freq[ord(ele) - ord("a")] += 1

        scores = collections.defaultdict(int)
        for index, value in enumerate(score):
            scores[index] = value

        def dfs(index):
            if index == len(words):
                return 0
            nonlocal freq
            res = 0
            # exclude
            res = max(res, dfs(index + 1))
            # include
            temp_dict, feasible, score_added = freq.copy(), True, 0
            for j in range(len(words[index])):
                if freq[ord(words[index][j]) - ord("a")] > 0:
                    freq[ord(words[index][j]) - ord("a")] -= 1
                    score_added += scores[ord(words[index][j]) - ord("a")]
                else:
                    feasible = False
                    break
            if feasible:
                res = max(res, score_added + dfs(index + 1))
            freq = temp_dict

            return res

        return dfs(0)
