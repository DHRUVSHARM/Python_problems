# counting based question 
"""
we need to find the kth smalles lexicographic palindromic permutation 
the permutation formula counts similar permutations with repitions 

total! / (freq1! * freq2! * freq3!) where these are repeating frequencies 

we know s is palindromic

so we dont need to consider middle element ,since it is required to stay put for all the permutations 

we can iterate till len // 2
since every permutation uniquely identifies the mirror image 



start = (len(s)) ! / (mul sum of the freq )


# first we need to get the half length and calculate all the factorials until that point 



"""


import collections
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s) // 2
        fact = [1] * (n + 1)

        for i in range(1 , len(fact)):
            fact[i] = (fact[i - 1] * i)
        
        res = []

        # we need to calculate the initial number 
        freq = collections.defaultdict(int)
        for i in range(0 , n):
            freq[s[i]] += 1
        
        denom = 1
        for v in freq.values():
            denom *= fact[v]
        
        current_perms = fact[n] // denom
        ans = []

        while n:
            # we select the right group where we can place the curren element 
            # we are only working with the first half 
            seen = False
            for ch in range(0 , 26):
                element = chr(ch + ord('a'))
                if freq[element] == 0:
                    continue
                group_size = (freq[element] * current_perms) // n

                if k - group_size <= 0:
                    # belong to this group , so k will remain the same 
                    # but we will have smaller group to look at 
                    # print(element , " : " , group_size , " : " , k)
                    # print(freq)

                    ans.append(element)
                    seen = True
                    freq[element] -= 1
                    current_perms = group_size
                    break
                else:
                    k -= group_size # warning 


            if not seen:
                # print(ans , " : " , n)
                break

            n -= 1 # reduce the length 

        # ngyygn
        """
        n   g   y | y   g   n
        """
        # print("ans : " , "".join(ans))

        if n > 0:
            return ""
        else:
            if len(s) % 2 == 1:
                ans = ans + [s[len(s)//2]] + list(reversed(ans))
            else:
                ans = ans + list(reversed(ans))

            return "".join(ans)