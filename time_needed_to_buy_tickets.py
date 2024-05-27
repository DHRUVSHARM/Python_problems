from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sentinel, ans = tickets[k] - 1, 0
        for index, element in enumerate(tickets):
            tickets_used = element - max(0, (element - sentinel))
            # tickets left = element - tickets_used
            tickets[index] = max(0, (element - sentinel))
            ans += tickets_used

        # this is imp as this depends on the position
        sentinel = 1
        for index in range(0, k + 1):
            # here we only care about tickets used
            ans += tickets[index] - max(0, (tickets[index] - sentinel))

        # print("tickets : ", tickets)
        return ans
