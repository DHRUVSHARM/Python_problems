if __name__ == '__main__':
    s = "dhruv"
    for i in range(len(s) + 1):
        print("the two parts are : ", s[:i], " :::: ", s[i:])

    print(s.count("d"))


class Solution:
    def maxScore(self, s: str) -> int:
        ans = float("-inf")
        left_score = 0
        # number of zeroes here
        right_score = s.count("1")
        # number of ones here

        for index in range(0, len(s) - 1):
            left_score += (1 if s[index] == "0" else 0)
            right_score -= (1 if s[index] == "1" else 0)

            ans = max(ans, left_score + right_score)

        return ans