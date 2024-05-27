import collections
from typing import List

if __name__ == '__main__':
    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    words.sort(key=lambda w: len(w))
    print(words)

    x = "a"
    for i in range(0, len(x)):
        print("word :")
        print(x[:i] + "" + x[i + 1:])


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        dp = collections.defaultdict(int)
        dp[""] = 0
        # base case
        for w in words:
            # print(dp)
            for index in range(len(w)):
                dp[w] = max(dp[w] ,
                dp.get(
                    w[:index] + "" + w[index + 1:],
                    0
                ) + 1
                )

        max_length = 0
        for length in dp.values():
            max_length = max(max_length, length)

        return max_length