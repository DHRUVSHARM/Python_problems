class Solution:
    def minimumLength(self, s: str) -> int:
        ans, i, j = len(s), 0, len(s) - 1
        while i < j and s[i] == s[j]:

            temp_left, temp_right = i, j
            # some intermediate situation
            prev = s[i]

            while i < temp_right and s[i] == prev:
                i += 1

            while j > temp_left and s[j] == prev:
                j -= 1

        return 0 if i > j else j - i + 1
