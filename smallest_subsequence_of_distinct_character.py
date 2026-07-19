"""
Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"



lexicographically smalles sequence 


assume that we have one atleast for each 
pull out the (  smallest ord    ,   smallest index )
hold a current index  



"c  b   a   c   d   c   b   c"


Input: s = "    c   b   a   c   d   c   b   c   "




Output: "   a   c   d  b   "





a  c d | b  

"""
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        last_seen = {}
        seen = set()

        for index , element in enumerate(s):
            last_seen[element] = index # always pick the last element 
        

        for index, element in enumerate(s):
            if element in seen:
                continue

            while len(st) and ord(element) < ord(st[-1]) and last_seen[st[-1]] > index:
                # if element is already fixed then useful to keep the earlier one anyways 
                # if we have a smaller incoming element that is not considered and it can be found later 
                seen.remove(st[-1])
                st.pop()
                
        
            st.append(element)
            seen.add(element)

        return "".join(st)