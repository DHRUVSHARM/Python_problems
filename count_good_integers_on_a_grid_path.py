import collections
class Solution:

    def helper(self, limit:list[int] , is_criticial:list[bool])->int:
        # return the count of good numbers using digit dp
        # num_bound : the 16 pos limit with leading zeroes 
        # is_critical : boolean arr of 16 pos that indicates the critical indices in the traversal 
        """
        map will indicate the positions 
        [0  0   0   0   0   0   1   2   3   ..]
        
        dp[0][1][-1] no prev element seen 

        keep a track of prev index 


        """
        # print(limit)
        # print("is critical : " , is_criticial)
        dp = collections.defaultdict(int)
        dp[(0 , 1 , -1)] = 1

        for pos in range(0 , 16):
            for tight in range(0 , 2):
                for prev in range(-1 , 10):
                    # need to decide which digits to put 
                    lim = limit[pos] if tight == 1 else 9 # if tight == 0 then we are free to put digits here 
                    
                    for digit in range(0 , lim + 1):
                        # possible digits on the current pos 
                        # new tight depends on previous tight and current chosen tight 
                        new_tight = tight and (digit == lim)
                        if is_criticial[pos]:
                            # need to respect monotonicty , the newprev will be digit now, if digit >= prev
                            # if prev is -1 then put as digit 
                            if prev == -1:
                                dp[(pos + 1 , new_tight , digit)] += dp[(pos , tight , prev)]
                            else:
                                # otherwise we will make the addition iff, this digit is >= prev
                                dp[(pos + 1 , new_tight , digit)] += (dp[(pos , tight , prev)] if digit >= prev else 0)
                        else:
                            # can keep the previous push forward
                            dp[(pos + 1 , new_tight , prev)] += dp[(pos , tight , prev)]
                    
        
        # over all the pos = 15 , tight 0/1 , and prev values available, sum 
        # we know that the number at 0 , 0 is at least the critical index , and will be a digit 
        # -1 was used for sentinel only
        ans = 0
        for prev in range(0 , 10):
            ans = ans + dp[(16 , 0 , prev)] + dp[(16 , 1, prev)]
        
        return ans

    def prepend_num(self, num:int)->list[int]:
        digits = []
        while num:
            dig = num % 10
            num = num // 10
            digits.append(dig)
        
        zeroes = 16 - len(digits)
        while zeroes:
            digits.append(0)
            zeroes -= 1
        
        digits.reverse()
        return digits

    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # preprocessing 
        l_limit , r_limit = self.prepend_num(l - 1) , self.prepend_num(r)
        critical_map = [False for _ in range(16)] # map 

        r , c = 0 , 0
        critical_map[0] = True # always critical 
        for element in directions:
            if element == 'D':
                r , c = r + 1 , c
            else:
                r , c = r , c + 1
            critical_map[r*4 + c] = True
        
        return self.helper(r_limit , critical_map) - self.helper(l_limit , critical_map)