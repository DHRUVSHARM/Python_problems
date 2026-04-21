"""
Given a string containing 
just the characters '(' and ')', 
return the length of the longest valid (well-formed) parentheses substring.

                                  
            -1   0    5   
Input: s = ")    )    )   (     (     ("


Output: 4
Explanation: The longest valid parentheses substring is "()()".
            
            
            0   1   2   3   4   5

            
            
            Input: s = ")   (   )   (   )   )"
last seen index = 0

-1  0   1   2
)   (   (   )


) 

2 - 0 = 2

Example 1:


-1      0  
        (  



-1  0               
)   (     


Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:


if front 

-1   0   5

 )   )   )

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st , result = [(-1 , ")")] , 0

        for index, element in enumerate(s):
            # print(st)
            add = True
            if element == ")":
                if st[-1][1] == "(":
                    # can close () 
                    result = max(result , index - st[-2][0])
                    st.pop()
                    add = False
                    pass
                else:
                    # )) 
                    pass
            else:
                # open incoming ( 
                if st[-1][1] == "(":
                    # ((
                    pass
                else:
                    # )(
                    pass
            
            if add:
                st.append((index , element))

        return result

        