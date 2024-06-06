import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = collections.deque(range(0, len(deck)))
        result = [0 for _ in range(0, len(deck))]

        for element in deck:
            # for every element we pop from the queue and push the next to the back
            top = q.popleft()
            if q:
                second = q.popleft()
                q.append(second)

            result[top] = element

        return result
