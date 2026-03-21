"""
l        r
xxxxadobec


increase till found, r , then stop , current == need
move the l till conditon is false keep considering in the loop , current != need 

add check 

while left <= right and condition satisfiedd
    consider
    new calc move


                                                l            r   
Input: s = "A   D   O   B   E   C   O   D   E   B   A   N   C", t = "ABC"

                            total needed = 3
                            fixed 
                            need 
                            a : 1
                            b : 1
                            c : 1

                            current total = 2
                            have 
                            a : 1
                            d : 1
                            o : 1
                            b : 1
                            e : 1
                            c : 0

                            key should actually be needed 
                            if current freq <= need += 1
                            if current freq <= need -= 1
result = L , R
Output: "BANC"

complexity analysis : n * (m * n)

Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result , left , need , curr , total_need , total_curr = (0 , len(s)) , 0 , collections.defaultdict() , collections.defaultdict() , 0 , 0
        
        # need is fixed , simple freq count 
        for element in t:
            if element not in need:
                need[element] = 0
            need[element] += 1
            total_need += 1
        
        # print("need")
        # print(need)
        # print("total need : " , total_need)

        for r in range(0 , len(s)):
            element = s[r]
            if element not in curr:
                curr[element] = 0
            curr[element] += 1

            if element in need:
                # we need to consider
                if curr[element] <= need[element]:
                    total_curr += 1
            
            # while the window is stil valid
            while left <= r and total_curr == total_need:
                
                # consider
                i , j = result
                if (r - left + 1) <= (j - i + 1):
                    result = (left , r)
                    # print("here : " , result)

                # now shift the left pointer
                curr[s[left]] -= 1
                if s[left] in need:
                    if curr[s[left]] < need[s[left]]:
                        total_curr -= 1

                left += 1 
            
        
        i , j = result
        if i == 0 and j == len(s):
            return ""
        else:
            return s[i : j + 1]