"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

dp(i , j) = match from [0 ... i] the pattern to be used is [....j]
# guarantee that we will have * only after a letter or . so that is covered 


            
            

note both s and p size will be atleast one

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.




consecutive *** for patterns can be replaced with single 
a***abc
0 or more (0 or more (0 or more a)))) -> 0 or more a  

dp[(-1 , -1)] = empty match empty implies true 

dp[(-1 , 0)]
s = ""
p = first element , always an alphabet or maybe . in which case we put true else false 

if one elemetn, always false
need to check the first two otherwise to make true if we have element* since 0 is possible 

dp[(0 , -1)]
s = a lower case english letter 
p = "" , nothing 
always false 
for all indices from 0 to len(s)


dp[i][j] = if p[j] == "*" : 
                check with the prev part in pattern and current s and move forward with true if possible
                if . handle
                dp[i - 1][j]

                also or 
                dp[i][j - 2] to skip totally as well

            if p[j] == "."
                walkover letter match , both move back 
                dp[i - 1][j - 1] 

            if character then char match 
                dp[i - 1][j - 1]


"""
import collections
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # preprocess
        temp , index = [] , 0
        while index < len(p):
            if index != 0 and p[index - 1] == "*" and p[index] == "*":
                # do not add multiple stars
                pass
            else:
                # normal add
                temp.append(p[index])
            index += 1
        
        # replace with corrected pattern for edge case matching 
        p = "".join(temp)
        # print(p)

        dp = collections.defaultdict()

        # base cases 
        dp[(-1 , -1)] = True

        for index in range(0  , len(s)):
            # empty pattern can never match 
            dp[(index , -1)] = False
        
        dp[(-1 , 0)] = True if p[0] == "." else False

        if len(p) > 1:
            dp[(-1 , 1)] = True if p[1] == "*" else False
        
        for index in range(2 , len(p)):
            if p[index] == "*":
                dp[(-1 , index)] = dp[(-1 , index - 2)]
            else:
                dp[(-1 , index)] = False
            

        for i in range(len(s)):
            for j in range(len(p)):
                result = False
                if p[j] == ".":
                    # can always match 
                    result = result or (True and dp[(i - 1  , j - 1)])
                elif p[j] == "*":
                    # check if we can match with previous element  
                    result = result or ( (s[i] == p[j - 1] if p[j-1] != "." else True) and dp[(i - 1 , j)])   
                    # also we can skip completely to consider the zero case 
                    result = result or dp[(i , j - 2)]
                else:
                    # simple character match 
                    result = result or ( (s[i] == p[j]) and dp[(i - 1 , j - 1)] )
                dp[(i , j)] = result

        # print(dp)
        return dp[(len(s) - 1 , len(p) - 1)]




        