"""

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b



a                   b
a a b c c          d b b c a

a a  d b b c b c a c


0 , 0  -1 , 0
        0 , -1

dp[i][j][i+j] = possible to interleave a[..i] , b[...j] to form c[,,,i+j] correctly 

dp[0][0][0] = True

len(a) * len(b)


"""
import collections
class Solution:

    def mcm_traversal(self , m , n):
        # traversing upper half diagonal elements m x n
        for off in range(0 , n):
            i , j = 0 , 0 + off
            while j < n:
                print(i , " : " , j)
                i += 1
                j += 1
            print("\n")

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m , n = len(s1) , len(s2)
        dp = collections.defaultdict()

        if (m + n) != len(s3):
            return False

        # base cases
        dp[(-1 , -1)] = True

        # direct comparision if any one is empty 
        for i in range(0 , m):
            dp[(i , -1)] = (s1[i] == s3[i]) and dp[(i - 1 , -1)]

        for j in range(0 , n):
            dp[(-1 , j)] = (s2[j] == s3[j]) and dp[(-1 , j - 1)]

        for i in range(0 , m):
            for j in range(0 , n):
                result = False
                if (i + j + 1) < len(s3):
                    result = result or  (s1[i] == s3[i + j + 1]) and dp.get((i - 1 , j) , False)
                    result = result or  ( s2[j] == s3[i + j + 1]) and dp.get((i , j - 1) , False)

                dp[(i , j)] = result


        return dp.get((m - 1 , n - 1) , False)

