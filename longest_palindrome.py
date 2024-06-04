import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = collections.defaultdict(int)
        for element in s:
            freq[element] += 1

        ans, center = 0, False
        for val in sorted(freq.values(), key=lambda v: -1 * v):
            if val % 2 == 0:
                ans += val
            elif center:
                ans += val - 1
            else:
                ans += val
                center = True

        return ans


a = {"a": 4, "b": 1, "c": 2, "d": 100}
for key, val in sorted(a.items(), key=lambda element: -1 * element[1]):
    print(key, " : ", val)
