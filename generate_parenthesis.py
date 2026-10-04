class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        given n pairs, 
        we have n open and n closed parenthesis 
        if balanc < 0 prune 
        when both are n and balance == 0 then add it 
        """

        ans = []

        def helper(n , curr , balance):
            
            # print("curr : " , curr , " " , "balance : " , balance)
            
            if balance == -1 or balance > n or len(curr) > (2*n):
                return # dont add if more close or more open than we can close or we dont want any combination 
                # greater than max allowed length to creep in as well
            
            if (len(curr) == 2*n) and balance == 0:
                # add
                ans.append("".join(curr))
                return

            # backtrack
            # add open bracket
            curr.append("(")
            helper(n , curr , balance + 1)
            curr.pop()

            # add closed bracket 
            curr.append(')')
            helper(n , curr, balance - 1)
            curr.pop()



        helper(n , [] , 0)
        return ans