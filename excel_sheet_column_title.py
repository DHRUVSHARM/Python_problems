if __name__ == "__main__":
    element = "A"
    e = chr(ord("A") + 1)
    print(e)
    dictionary = {i: chr(ord("A") + i - 1) for i in range(1, 27)}
    print(dictionary)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        # using mod gives us the lsb in a number system, and dividing is like the
        # right shift , multiplying is left shift ( all ops by base of the number system)
        # 0 based since we use mod and all
        while columnNumber:
            result = chr(ord("A") + (columnNumber - 1) % 26) + result
            columnNumber = (columnNumber - 1) // 26

        return result
