"""

You are given a binary string s of length n, where:

'1' represents an active section.

'0' represents an inactive section.


You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.


0   111111  0   -> 0    000000  0

Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.


TTTTTTTTFFFFFF

say we try to do with 

0       n + 1
true     false 

l          r

return l 

0   1   1   1   1   1   2   2     2
        l                   r
1 | 1   0   0   0   1   0   0   | 1



        3                  2                  2                                 7                           4   
1   |   ......  0   0   .....   0   0   0   ......  0   0   0   0   0   .....................   0   0   ........    0   0   0   |   1

(0 , 0)         

        1       3       6    7             11   12                     18                   25           28    31     

0 and prev is 1 or 0 and next is 1 add the index 

"""
"""

You are given a binary string s of length n, where:

'1' represents an active section.

'0' represents an inactive section.


You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.


0   111111  0   -> 0    000000  0

Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.


TTTTTTTTFFFFFF

say we try to do with 

0       n + 1
true     false 

l          r

return l 

0   1   1   1   1   1   2   2     2
        l                   r
1 | 1   0   0   0   1   0   0   | 1



        3                  2                  2                                 7                           4   
1   |   ......  0   0   .....   0   0   0   ......  0   0   0   0   0   .....................   0   0   ........    0   0   0   |   1

(0 , 0)         

        1       3       6    7             11   12                     18                   25           28    31     

0 and prev is 1 or 0 and next is 1 add the index 

"""
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        new_arr = [1] + [ord(c) - ord('0') for c in s] + [1]

        # store the open and close pairs 
        opened = False # start with opened false 
        active = 0
        zero_intervals = []
        for index, element in enumerate(new_arr):
            if element == 0:
                if not opened:
                    zero_intervals.append([index, None])
                    opened = True
            
                if new_arr[index + 1] == 1:
                    # need to close
                    opened = False
                    # apply the closing logic and append
                    zero_intervals[-1][1] = index
            else:
                # 1 case we move along 
                active += 1
        
        # print("zero intervals : " , zero_intervals)
        # print("active : " , active)
        max_change = 0 
        # now we hae [open , close] , [open1 , close1] , ... of zeroes 
        for index in range(1 , len(zero_intervals)):
            cs , ce = zero_intervals[index]
            ps , pe = zero_intervals[index - 1]
            
            max_change = max(
                max_change , 
                (ce - ps + 1) - (cs - pe - 1) # added ones 
            )
        
        return active + max_change - 2