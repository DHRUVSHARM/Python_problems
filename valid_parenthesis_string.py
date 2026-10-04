class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        very important style of problem where we look at brackets and a wildcard character 
        to think about valid parenthesis strings 

        Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

        The following rules define a valid string:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
        
        think about the problem like this 
        1) at every point we need the balance to be > 0
        2) the 2 major cases are if we use all the * for a closing  (to close out max excesses) or we
        use all the * for opening to have the max open 

        Example 1:

        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "(*)"
        Output: true
        Example 3:

        here say we do it we end up with 1 +1  - 1 = 1 
        since we have an empty, we need some way to track that, but the idea is an empty 
        we may need to keep track of open conversions 
        and closed conversions 



        Input: s = "(*))"
        Output: true
        Example 4:

        Input: s = "("
        Output: false
        

        Constraints:

        1 <= s.length <= 100
        s[i] is '(', ')' or '*'.

        1) if closed > 0 means never possible to close all so return false 
        2) if open result considered and it is greater than 0 we need to look at the count of * to see how many flipped to open
        flipping a * to close means subtract 2 from the result we want to see if that can be zero 
        and if we decide to put remaining as empty then ok 
        ultimately try to reduce open to 0 is the best case scenarion here 
        if open < 0 again finished no way to counter all the fixed closed so false 

        """
        empty_slot_count = 0
        n = len(s)

        open_res = 0
        close_res = 0

        for element in s:
            if element == '(':
                open_res += 1
                close_res += 1
            elif element == ')':
                close_res -= 1
                open_res -= 1
            else:
                # empty slot 
                empty_slot_count += 1
                open_res += 1
                close_res -= 1

            close_res = max(close_res , 0) # keep it clamped to 0 
            # so we can keep the range up 

            if open_res < 0:
                # need to maintain the upper bound to >= 0
                return False

            """
            ideas : range generation continuos, select element at each level ,
            empty : generated 
            -1 , shift left all
            +1 , shift right all
            """

        return close_res == 0