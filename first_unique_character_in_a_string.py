import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = collections.defaultdict(list)

        for index, val in enumerate(s):
            if val not in repeat:
                # store by initializing with 0 and storing the first index of occurence
                repeat[val] = [0, index]

            repeat[val][0] += 1

        ans = len(s)
        for freq, f_oc_i in repeat.values():
            if freq == 1:
                ans = min(ans, f_oc_i)

        return -1 if ans == len(s) else ans
