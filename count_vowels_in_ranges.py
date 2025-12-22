from typing import List



class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = {0 : 0 for _ in range(0 , len(words))}
        dp[-1] = 0

        vowels = set(['a' , 'e' , 'i' , 'o' , 'u'])

        for index , element in enumerate(words):
            dp[index] = dp[index - 1] + (
                1 if (element[0] in vowels and element[-1] in vowels) else 0
            )
        
        ans = []
        for l , r in queries:
            ans.append(dp[r] - dp[l - 1])

        return ans