import collections
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq, n = collections.defaultdict(int), len(words)
        for word in words:
            for letter in word:
                freq[letter] += 1

        for value in freq.values():
            if value % n != 0:
                return False

        return True
