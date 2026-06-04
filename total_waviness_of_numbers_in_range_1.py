class Solution:
    
    def helper(self, num):
        # log 10 convert to list 
        res = []
        while num:
            res.append(num % 10)
            num = num // 10
        
        res.reverse()
        ans = 0

        for index in range(1 , len(res) - 1):
            if (res[index - 1] < res[index] > res[index + 1]) or (res[index - 1] > res[index] < res[index + 1]):
                ans += 1
        
        return ans

    
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(num1 , num2 + 1):
            res += self.helper(num)
        
        return res