class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full, empty, ans = numBottles, 0, 0
        while (full + empty) >= numExchange:
            ans += full  # drink the full bottles
            full, empty = (full + empty) // numExchange, (full + empty) % numExchange
            # take the full + empty -> full bottles
            # print(full , " , " , empty)

        return ans + (full)
