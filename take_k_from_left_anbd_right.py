import collections


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        for element in s:
            freq[element] += 1
        
        def check():
            # print(freq)
            return freq['a'] >= k and freq['b'] >= k and freq['c'] >= k
        
        if not check():
            return -1

        ans , l = len(s) , 0

        for r in range(0 , len(s)):
            freq[s[r]] -= 1
            
            while l <= r and not check():
                freq[s[l]] += 1
                l += 1

            # print("l , r : " , l , " , " , r , " removals : " , l + len(s) - r - 1)
            ans = min(
                ans,
                l + len(s) - r - 1
            )


        return ans

