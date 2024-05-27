from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j, w1, w2 = 0, 0, 0, 0

        while i < len(word1) and j < len(word2):
            if word1[i][w1] != word2[j][w2]:
                return False

            w1 += 1
            w2 += 1

            if w1 == len(word1[i]):
                i += 1
                w1 = 0

            if w2 == len(word2[j]):
                j += 1
                w2 = 0

        return i == len(word1) and j == len(word2)