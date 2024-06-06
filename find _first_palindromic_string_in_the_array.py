from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word) - 1
            ispalin = True
            while i < j:
                if word[i] != word[j]:
                    ispalin = False
                    break
                i += 1
                j -= 1

            if ispalin:
                return word

        return ""
