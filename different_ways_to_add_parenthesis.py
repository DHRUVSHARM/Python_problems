from posixpath import split
from typing import List
from itertools import product


print(ord("2") - ord("0"))
# print("2" - "0")

operation_mapper = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

print(operation_mapper["*"](3, 7))

# cross product
a = [1, 2, 3]
b = [1, 2, 3]

c = list(map(lambda x: [(x, y) for y in b], a))
# destructuring
c = [item for sublist in c for item in sublist]
print(c)

# print(product(a, b))

# c = [(x, y) for x, y in product(a, b)]

# print(c)


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression_list = []

        l, r = 0, 0

        while r < len(expression):
            if expression[r] == "*" or expression[r] == "+" or expression[r] == "-":
                expression_list.append(int(expression[l:r]))
                expression_list.append(expression[r])
                l = r + 1

            r += 1

        expression_list.append(int(expression[l:r]))

        # print(expression_list)

        operation_mapper = {
            "*": lambda x, y: x * y,
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }

        def helper(arr):
            if len(arr) == 1:
                return arr

            result = []
            index = 2
            # ((0 ... index - 2) .. (index .. len(arr) - 1))
            while index < len(arr):
                left_result = helper(arr[0 : index - 1])
                right_result = helper(arr[index:])

                subresult = list(
                    map(
                        lambda lr: [
                            operation_mapper[arr[index - 1]](lr, rr)
                            for rr in right_result
                        ],
                        left_result,
                    )
                )
                # print(subresult)
                for sr in subresult:
                    result.extend(sr)

                index += 2

            return result

        return helper(expression_list)
