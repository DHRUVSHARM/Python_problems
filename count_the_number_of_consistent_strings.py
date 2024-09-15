from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        mask = 0
        for letter in allowed:
            mask = mask | (1 << (ord(letter) - ord("a")))

        ans = 0
        for word in words:
            consistent = True
            for letter in word:
                if (1 << (ord(letter) - ord("a"))) & mask:
                    pass
                else:
                    consistent = False
                    break

            if consistent:
                ans += 1

        return ans
