if __name__ == '__main__':
    t = "dhruv"
    print(t[:len(t)])


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small, large = str1, str2
        if len(small) > len(large):
            small, large = large, small

        res = ""
        for i in range(len(small) - 1, -1, -1):
            divisor = small[:i + 1]
            if len(small) % len(divisor) == 0 and len(large) % len(divisor) == 0 and divisor * (
                    len(small) // len(divisor)) == small and divisor * (len(large) // len(divisor)) == large:
                # worst case o(len(large) + len(small))
                res = divisor
                break

        return res
