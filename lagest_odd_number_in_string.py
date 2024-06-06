class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = {"1", "3", "5", "7", "9"}
        index = len(num) - 1
        while index >= 0:
            if num[index] in odd:
                break
            index -= 1

        return num[0 : index + 1]
