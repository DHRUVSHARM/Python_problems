import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = collections.Counter(chars)
        ans = 0
        for word in words:
            word_count, possible = collections.Counter(word), True

            for w, f in word_count.items():
                if not (w in char_count and char_count[w]) >= f:
                    possible = False
                    break

            ans += len(word) if possible else 0

        return ans
