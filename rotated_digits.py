"""
// brute force solution 
class Solution:

    def rotatedDigits(self, n: int) -> int:
        # brute force 
        # number -> some rotate to same, some to diff -> if all same : bad , else good if even one place changes 
        # brute forc 10*4 multiply check each digit
        
        
        same_map , diff_map = {0 , 1 , 8} , {2 , 5 , 6 , 9}
        
        result = 0

        def helper(num):
            ans = False

            while num:
                digit = num % 10
                num = num // 10
                if digit in diff_map:
                    ans = True
                elif digit not in same_map:
                    ans = False
                    break # invalid
            
            return ans

        for i in range(1 , n + 1):
            if helper(i):
                result += 1
        
        return result
"""



# digit dp solution 
# pos , tight , changed 
# tight = 0 , 1 not tight , tight 
# changed = 0 , 1 not changed , changed 

# base case :
# _ 0 index, pos = 0 , tight = 1 , changed = 0
# indices range from 1 to n , indices will map from 0 - 1 , so on 
import collections
class Solution:

    def num_to_digits(self, num):
        ans = []
        while num:
            digit = num % 10
            ans.append(digit)
            num = num // 10
        ans.reverse()
        return ans

    def rotatedDigits(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[(0 , 1 , 0)] = 1 # base case 

        digits = self.num_to_digits(n)
        same_map , diff_map = {0 , 1 , 8} , {2 , 5 , 6 , 9}

        for pos in range(0 , len(digits)):
            for tight in range(0 , 2):
                for changed in range(0 , 2):

                    limit = 9 if tight == 0 else digits[pos]

                    for d in range(0 , limit + 1):
                        # put d at current pos, retro calculate relation with prev state to add into current state 
                        if d not in same_map and d not in diff_map:
                            continue # invalid digit 
                        
                        new_tight = tight and d == digits[pos]
                        new_changed = changed or d in diff_map

                        dp[(pos + 1 , new_tight , new_changed)] += dp[(pos , tight , changed)]

        return dp[(len(digits) , 0 , 1)] + dp[(len(digits) , 1 , 1)]