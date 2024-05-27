if __name__ == '__main__':
    s = "dhruv"
    print(s[1])


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left, right, left_backspace, right_backspace = len(s) - 1, len(t) - 1, 0, 0
        while left >= 0 or right >= 0:
            if left >= 0 and s[left] == '#':
                left_backspace += 1
                left -= 1
            elif right >= 0 and t[right] == '#':
                right_backspace += 1
                right -= 1
            elif left_backspace > 0:
                left -= 1
                left_backspace -= 1
            elif right_backspace > 0:
                right -= 1
                right_backspace -= 1
            else:
                if left >= 0 and right >= 0 and (s[left] == t[right]):
                    left -= 1
                    right -= 1
                else:
                    return False

        return True