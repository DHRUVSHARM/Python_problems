class Solution:
    def numSteps(self, s: str) -> int:
        s, index = list(s), len(s) - 1
        carry, ans = 0, 0

        while index > 0:
            element = 0 if s[index] == "0" else 1
            # print("element : " , element , " , " , "carry : " , carry)
            element = element + carry
            carry = 0
            if element % 2:
                # odd number need to add one , and move
                ans += 2
                carry = 1
            else:
                # even number
                carry = 1 if element == 2 else 0
                ans += 1
                # print(ans)
            index -= 1

        element = 1  # guarantee
        # print(element , " , " , carry)
        element = element + carry

        ans += 0 if element == 1 else 1

        return ans
