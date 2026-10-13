class Solution:
    def calculate(self, s: str) -> int:
        """
        (1+(4+5+2)-3)+(6+8)

        acc = 0

        """

        acc , st = 0 , []
        curr_digit , sign = 0 , 0

        # running state is recorded with acc, sign 
        # idea is to use stack frames to pause and record new state, there will be a reset once something is pushed
        # need to handle edge cases as is 

        for element in s:
            if element == ' ':
                continue
            elif element == '(' or element == ')':
                pass
            elif element == '+' or element == '-':
                # sign will change here 
                pass
            else:
                # digit can keep adding, will need to reset this 
                curr_digit += (10 * curr_digit + ord(element) - ord('0'))