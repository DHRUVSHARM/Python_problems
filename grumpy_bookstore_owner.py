from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # first we will calculate the score which is given
        score_guaranteed = 0
        for index in range(0, len(customers)):
            if not grumpy[index]:
                score_guaranteed += customers[index]

        ans, index, curr = 0, 0, 0
        # now we will move a fixed window

        while index < minutes:
            curr += customers[index]
            if not grumpy[index]:
                score_guaranteed -= customers[index]
            index += 1

        ans = max(ans, score_guaranteed + curr)

        start_index = 0

        while index < len(customers):
            curr += customers[index]
            curr -= customers[start_index]

            if not grumpy[start_index]:
                score_guaranteed += customers[start_index]

            if not grumpy[index]:
                score_guaranteed -= customers[index]

            index += 1
            start_index += 1

            ans = max(ans, score_guaranteed + curr)

        return ans
