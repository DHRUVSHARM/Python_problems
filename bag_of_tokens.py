from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans, score, left, right = 0, 0, 0, len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                ans = max(ans, score)
                # can be added to score
            else:
                # to the right we have a token which is definitely greater than the
                # token we are trying to overcome , we should take the largest boost to overcome
                if score:
                    power += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    # we cannot absorb anything to overcome tokens[left] ,can break here
                    break

        return ans
