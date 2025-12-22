class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        brackets , ans = [] , 0

        for element in s:
            if element == '(':
                # opening bracket so add it none the less ...
                brackets.append('(')
            else:
                if not brackets:
                    ans += 1
                else:
                    brackets.pop()

        ans += len(brackets)    

        return ans