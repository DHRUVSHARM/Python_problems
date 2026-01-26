"""
Example 1:

Input: s = "00110"
            
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.

"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # keep track of the global result, and we keep track of 
        result , ones = 0 , 0

        for element in s:
            if element == '1':
                # is we already have the minimal flips calculated + 1 , so does not matter
                # only increment ones
                ones += 1
            else:
                # we have seen a 0 so now we have to decide 
                # flip to one = 1 + s[..i-1] (min flips)
                # keep 0, we expect everything behind to be 0 as well we have ones for that reason 
                result = min(
                    1 + result,
                    ones                    
                )

        return result

        