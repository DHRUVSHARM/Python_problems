import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = collections.Counter(words[0])

        for index in range(1, len(words)):
            word = words[index]
            curr_freq = collections.Counter(word)

            for key in curr_freq.keys():
                curr_freq[key] = min(curr_freq[key], ans[key])

            ans = curr_freq

        result = []
        for key in ans.keys():
            occur = ans[key]
            while occur:
                result.append(key)
                occur -= 1

        return result
