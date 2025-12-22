class Solution:
    def numSub(self, s: str) -> int:
        left , ans , MOD = 0 , 0 , 10**9 + 7

        for r in range(0 , len(s)):
            if s[r] == '0':
                ans += ((r - left ) * (r - left + 1)) // 2
                left = r + 1 

        ans += ((len(s) - left ) * (len(s) - left + 1)) // 2
    

        return ans % MOD