if __name__ == '__main__':
    s = "dhruv"
    for index, value in enumerate(s):
        print("index : ", index, " , ", "value : ", value)


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for index , value in enumerate(s):
            # we will start to compare with the string of type : 010101...
            if index % 2 == 0:
                ans += 1 if value == "0" else 0
            else:
                ans += 1 if value == "1" else 0

        return min(ans , len(s) - ans)
