from typing import List


"""
Input: 


    0   1
s = "   1   0   2   0   3   0   0   4   ", 
        0   1   1   2   2   3   3   3 
    
    0   1   2    3   4

    0   1   12      123         1234
        1   2       3           4

queries = [[0,7],[1,3],[4,6]]




"""


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        
        s = [ord(c) - ord('0') for c in s]
        prev_non_zero = [0] * (len(s) + 1)
        pow_10 = [1]
        m = 10**9 + 7

        for _ in range(2 , 10**5 + 2):
            pow_10.append(  pow_10[-1]*10 % m )
        
       

        # digit sum will not require the s to be changed 
        prefix = 0
        digit_sum = []
        non_zero_prefix = [0]

        for index, element in enumerate(s):
            prefix += element
            digit_sum.append(prefix)
            if element != 0:
                non_zero_prefix.append( (non_zero_prefix[-1] * 10 + element) % m )

            if index > 0:
                prev_non_zero[index] += (prev_non_zero[index - 1] + (1 if s[index - 1] > 0 else 0))

        prev_non_zero[-1] += (prev_non_zero[-2] + (1 if s[-1] > 0 else 0))

        
        # print(non_zero_prefix)

        def helper(l , r):
            new_l , new_r = prev_non_zero[l] , prev_non_zero[r + 1]
            return non_zero_prefix[new_r] - non_zero_prefix[new_l] * (pow_10[new_r - new_l])

        ans = []
        for l , r in queries:
            d_sum = digit_sum[r] - (digit_sum[l - 1] if l >= 1 else 0)
            concat_num = helper(l , r)
            ans.append( (concat_num * d_sum) % m ) 

        return ans       

