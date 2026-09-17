class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # at every step we can compare the size of what we saw until now 
        """
        dp[i] = max(
            dp[i - 1],
            
        )

        dp[i] max number of non overlapping substrings considering 0 ... i with atleast k length
        dp[i] = dp[i - 1] # consider previous end 

        from i select i - (k - 1)

                i-(k-1)-1    i - (k - 1)             i

        so on thing is we need to check if (i - (k - 1)) .... i should be a palindrome (const time lookup)
        and if that is the case we may consider dp[i - (k - 1) - 1]
        this is considering size k ending at i 

        palindrom of size k = 3
                            111 enough to check k
                           1111 followed by k + 1

                          1 111 1 for something like this if we know this is a palindrome then either k or k + 1 is palindrome    
                            like in this case 

                            1   1111    1       here k + 1 is the center 
                            so means we can always decompose larger answers into the smallest centers k , k + 1
                            and those will always be better since they provide more span for the previous answers to build 

        so we only consider them, that also if k , k + 1 are palindromic 
        
        # for palindromic lookup , 
        we can use the odd even centers logic

        """
        n = len(s)
        is_palindrome = [[False for _ in range(0 , n)] for _ in range(0 , n)]
        # single element are palindrome and even lenght as well

        for i in range(0 , n):
            is_palindrome[i][i] = True
            if i + 1 < n:
                is_palindrome[i][i + 1] = (True if s[i] == s[i + 1] else False)


        for center in range(0 , n):
            # odd
            l , r = center , center
            while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                is_palindrome[l - 1][r + 1] = True
                l -= 1
                r += 1

            # even
            if center + 1 < n:
                l , r = center , center + 1
                if not is_palindrome[l][r]:
                    continue

                while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                    is_palindrome[l - 1][r + 1] = True
                    l -= 1
                    r += 1

        # at this point we have the lookup 
        dp = [0 for  _ in range(0 , n)]
        
        for index in range(0 , n):
            dp[index] = dp[index - 1] if (index - 1) >= 0 else 0 # simple skip consider 
            # consider k size 
            if index - (k - 1) >= 0 and is_palindrome[index - (k - 1)][index] == True:
                # is palindrome
                dp[index] = max(
                    dp[index],
                    (dp[index - (k - 1) - 1] if (index - (k - 1) - 1) >= 0 else 0) + 1 # consider current k size 
                )

            if index - (k) >= 0 and is_palindrome[index - (k)][index] == True:
                dp[index] = max(
                    dp[index],
                    (dp[index - (k) - 1] if (index - (k) - 1) >= 0 else 0) + 1  # consider k + 1 size 
                )
                  

        return dp[n - 1]
