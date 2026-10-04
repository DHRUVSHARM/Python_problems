class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        """
        we need to find the number of subrrays with odd sum
        best way to think about counting subarrays is using the ending at index point 
        """

        n = len(arr)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][arr[0] % 2] += 1

        for index in range(1 , n):
            dp[index][arr[index] % 2] += 1 # single element subarray 
            for rem in range(0 , 2):
                dp[index][(rem + arr[index])%2] += dp[index - 1][rem]

        return sum([dp[index][1] for index in range(n)]) % (10 ** 9 + 7)