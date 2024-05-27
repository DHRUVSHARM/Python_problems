if __name__ == '__main__':
    print(99 * 999)
    s = "dhruv"
    s = list(reversed(s))
    print(s)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums1 = list(reversed(num1))
        nums2 = list(reversed(num2))
        result = [0 for _ in range(len(nums1) + len(nums2))]

        def add_with_carry(number, index):
            carry = (result[index] + number) // 10
            result[index] = (result[index] + number) % 10
            # print(carry , result[index] , number)
            number = carry
            index += 1

            while carry != 0:
                # print("here")
                carry = (result[index] + number) // 10
                result[index] = (result[index] + number) % 10
                number = carry
                index += 1
            # print(number , result)

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                # now we need to add this
                index_of_insertion = i + j  # this is based on the number of zeroes
                add_with_carry(int(nums1[i]) * int(nums2[j]), index_of_insertion)

        # print(result)
        element = result[-1]
        while len(result) > 1 and element == 0:
            result.pop()
            element = result[-1]

        result = reversed(result)
        res = ""
        for ele in result:
            res += str(ele)

        return res