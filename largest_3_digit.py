if __name__ == "__main__":
    a = "7"
    print(ord(a) - ord("0"))


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        msb, index = "", -1

        for r in range(2, len(num)):

            if num[r] == num[r - 1] and num[r - 1] == num[r - 2]:
                # print(num[r-2 : r + 1])
                if msb == "":
                    index = r
                    msb = num[r - 2]
                else:
                    if ord(msb) - ord("0") < ord(num[r - 2]) - ord("0"):
                        index = r
                        msb = num[r - 2]

        return "" if index == -1 else num[index - 2 : index + 1]
