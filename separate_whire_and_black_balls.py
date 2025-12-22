class Solution:
    def minimumSteps(self, s: str) -> int:
        ans , one_count = 0 , 0

        for element in s:
            if element == '1':
                one_count += 1
            else:
                ans += one_count

        return ans
