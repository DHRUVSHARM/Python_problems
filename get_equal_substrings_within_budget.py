class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, ans, cost = 0, 0, 0

        for right in range(0, len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            while left <= right and cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left + 1)

        return ans
