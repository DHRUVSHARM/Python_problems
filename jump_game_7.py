"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. 
You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

dp[index] = (curr == 0) + (
    dp[max(0 , index - maxJump)] ... dp[index - minJump]

)

dp[0] = True
check if prefix[index - minJump] - prefix[max(0 , index - maxJump) - 1] < (index - minJump) - max(0 , index - maxJump) + 1
prefix[-1] = 0

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""


import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        dp = {0 : 0 for _ in range(0 , len(s))}
        dp[-1] = 0
        dp[0] = 1

        for index, element in enumerate(s):
            if index == 0:
                continue

            if element == '1' or index - minJump < 0:
                dp[index] = 0
            else:
                dp[index] = 1 if (dp[index - minJump] - dp[max(0 , index - maxJump) - 1] > 0) else 0
            
            if index == len(s) - 1:
                ans = dp[index]
            else:
                # current element is 0 and we have atleast one 0 in the previous window of possible start points for the current jump
                dp[index] += dp[index - 1]

        return ans > 0