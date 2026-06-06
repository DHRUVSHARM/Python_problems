import collections
class Solution:

    def helper(self, num):
        
        # convert to array of digits
        
        limit = []
        
        if num == 0:
            limit = [0]
        else:
            while num:
                digit = num % 10
                limit.append(digit)
                num = num // 10

        limit.reverse()

        # dp[(pos , start , tight, last, second last )]

        dp = collections.defaultdict(int)
        count = collections.defaultdict(int)

        dp[(0 , 0 , 1 , -1 , -1)] = 0 # this will represent the sum of all waviness 
        count[(0 , 0 , 1 , -1 , -1)] = 1 # will be useful to count  
        # initially we assume tight and not started 

        ans = 0
        for pos in range(0 , len(limit)):
            for start in range(0 , 2):
                for tight in range(0 , 2):

                    digit = limit[pos]                    
                    digit_limit = 9 if tight == 0 else digit

                    for curr_digit in range(0 , digit_limit + 1):
                        
                        
                        new_start = 1 if start == 1 or (start == 0 and curr_digit != 0 ) else 0 
                        new_tight = 1 if tight == 1 and curr_digit == digit else 0 
                        
                        for last_digit in range(-1 , 10):
                            for second_last_digit in range(-1 , 10):
                                # sld, ld, cd
                                # -1 are sentinel values that are not used to add to the complete sum 
                                # however the count of prefixes are added
                                # it is possible sum of these do not respect the tight constraint since 
                                # we are taking combinations of the last, second last, but the count will not be there  

                                if new_start == 0:
                                    # still not started
                                    new_last_digit = -1
                                    new_second_last_digit = -1
                                else:
                                    # new start is now 1 
                                    if start == 0:
                                        # first digit start 
                                        new_last_digit = curr_digit
                                        new_second_last_digit = -1
                                    else:
                                        # prev already started this is also 1 
                                        new_last_digit = curr_digit
                                        new_second_last_digit = last_digit
                                

                                count[(pos + 1 , new_start , new_tight , new_last_digit , new_second_last_digit)] += count[(pos , start, tight, last_digit, second_last_digit)]
                                
                                add = 1 if ((second_last_digit > last_digit < curr_digit or second_last_digit < last_digit > curr_digit) and (start == 1 and last_digit != -1 and second_last_digit != -1)) else 0
                                dp[(pos + 1 , new_start , new_tight , new_last_digit , new_second_last_digit)] += (add * count[(pos , start, tight, last_digit, second_last_digit)] + dp[(pos , start, tight, last_digit, second_last_digit)])
                                
  
        # ans over all combos 
            for tight in range(0 , 2):
                for last_digit in range(0 , 10):
                    for second_last_digit in range(0 , 10):
                        ans += dp[(len(limit) , 1 , tight , last_digit , second_last_digit)]

        return ans


    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.helper(num2) - self.helper(num1 - 1)