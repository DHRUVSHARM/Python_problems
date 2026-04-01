"""
solved with naive kmp initally 
time complexity : quadratic time (len haystack * len needle)

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



kmp ? 


s   a   b   b   u   t   s   a   d

s   a   d



lps [i] is the lenght of the longest prefix that we can have , 
behind the index i that is also a suffix 
    
        p                                  i 
a   a   a   c   a   a   a   c   c   a   a  a
0   1   2   0   1   2   3   4   0   1   2   


--------------------------------
        p    
a   a   a   a   a   a   
0   1   2   

0   1   2   3   4   5   6   7
a   a   a   x   a   a   a   a
            i

                            i - n + 1
a   a   a   a
            j

lps
0   1   2   3

if equal 
 lps[i] = lps[p] + 1 # the element at p is added to the prefix and current to suffix  

index
"sab    butsad", 


"sad"


----------------------------------------------------------------------------------------
TODO:  optimized kmp
"""


class Solution:
    # naive solution 
    def strStrNaive(self, haystack: str, needle: str) -> int:
        result = -1
        for i in range(0 , len(haystack)):
            start_index , found = i , True
            for j in range(0 , len(needle)):
                compare_index = start_index + j # use as offset 
                if compare_index < len(haystack) and haystack[compare_index] == needle[j]:
                    # in range, can compare and the comparision is successful 
                    pass
                else:
                    # we are still in the needle range, but something was finished and not complete 
                    found = False
            if found:
                result = start_index
                break
    
        return result

    # KMP implementation
    def strStr(self, haystack: str, needle: str) -> int:
        # calculate lps for the needle pattern initially 
        # m - text, n - pattern
        m , n = len(haystack) , len(needle)
        lps = [0 for _ in range(n)]

        # for index 0 already fixed , prev talks about front to consider  
        index , prev = 1 , 0

        while index < n:
            if needle[prev] == needle[index]:
                # can consider prev, index 
                prev += 1
                lps[index] = prev
                index += 1
            else:
                if prev == 0:
                    lps[index] = prev
                    index += 1
                else:
                    prev = lps[prev - 1] # go back to the prev 
            
        
        # match pattern
        i , j , start_index = 0 , 0 , -1

        # print(lps)

        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                # print("i : " , i , " " , "j : " , j)
                if j == len(needle):
                    start_index = i - n
                    break
                
            else:
                # need to move back j 
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        
        return start_index
