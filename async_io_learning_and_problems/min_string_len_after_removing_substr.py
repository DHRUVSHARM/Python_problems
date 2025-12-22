class Solution:
    def minLength(self, s: str) -> int:
        seen = [s[0]]
        for index in range(1 , len(s)):
            # print(seen)
            if s[index] == 'B' and seen and seen[-1] == 'A':
                seen.pop()
            elif s[index] == 'D' and seen and seen[-1] == 'C':
                seen.pop()
            else:
                seen.append(s[index])

        return len(seen)