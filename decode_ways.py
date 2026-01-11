class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        # print(s)
        # print(list(s))

        encoded = [ord(element) - ord('0') for element in list(s)]
        # print(encoded)

        dp[-1] = 1 

        # print(encoded)
        # print(dp)

        for index in range(len(s) - 1 , -1 , -1):
            if 1 <= encoded[index] <= 9:
                # consider the element at the index simply
                dp[index] += dp[index + 1]
            
            if (index + 2) < len(dp):
                if encoded[index] == 1 and 0 <= encoded[index + 1] <= 9:
                    dp[index] += dp[index + 2]
                elif encoded[index] == 2 and 0 <= encoded[index + 1] <= 6:
                    dp[index] += dp[index + 2]
        
        return dp[0]
    



if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("1012"))