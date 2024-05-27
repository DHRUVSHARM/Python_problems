class Solution:
    def reverseWords(self, s: str) -> str:
        s, left = list(s), 0

        def reverse_word(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        for r in range(0, len(s) + 1):
            if r == len(s) or s[r] == " ":
                # the end of the string or a space , indicating that a word
                # has been completed
                reverse_word(left, r - 1)
                left = r + 1

        return "".join(s)
