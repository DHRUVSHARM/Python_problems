

"""
simple seive logic to find till , n 
0   1   2   3   4   5   
f   f   t   t   t   t
"""

# precompute oustside the class once
def build_seive(limit):
    seive = [True]*(limit + 1)
    seive[0] = False
    seive[1] = False

    index = 2
    while index * index <= limit:
    
        if seive[index]:
            for j in range(index * index, len(seive) , index):
                seive[j] = False
        
        index += 1

    return seive

limit = 5 * 10**6 + 1 # from question 
seive = build_seive(limit)

class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0

        for num in range(0 , n):
            if seive[num]:
                ans += 1

        return ans