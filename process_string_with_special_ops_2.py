"""
If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.

        0   1   2   2   4   3   6 
Input: s = "c   d   %   #   *   #"  ,   k = 3

"""

class Solution:
    def processStr(self, s: str, k: int) -> str:
        # first we can build the index -> length map
        length = [0 for _ in range(len(s))]
        
        
        init_len = 0
        for i , element in enumerate(s):
            if element == '*':
                init_len -= 1 if init_len >= 1 else 0
            elif element == '#':
                init_len *= 2
            elif element == '%':
                pass
            else:
                init_len += 1
            length[i] = init_len
        

        # print("len : " , length)
        
        special = {'#' , '*' , '%'}
        # here k is the index that we want
        for index in range(len(s) - 1 , -1 , -1):
            
            if k >= length[index]:
                # not possible
                return '.'
            
            if k == length[index] - 1 and s[index] not in special:
                # found the index the character was added at this step
                return s[index]
            
            if s[index] == '*':
                # pop 
                # since k < len[index] - 1, should not affect it 
                pass
            elif s[index] == '#':
                k = (k - length[index]//2 + length[index]) % (length[index] // 2)
            elif s[index] == '%': 
                k = (length[index] - 1 - k)
            else:
                # lowercase 
                pass
            
            
        