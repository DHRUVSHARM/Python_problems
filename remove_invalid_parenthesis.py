"""

dfs approach 

find the minimal number of removals required
greedy :
monitor when balance becomes -1 , we need to add an extra open for sure at that point 
allow most of the opens to complete balancing with currently avaialble close points 

in the end when we have extra opens we need to have close added at the end 

so optimally the open and close can be found 

results can be made by backtracking 

if open == 0 , close == 0 and index == n and balance == 0 means we have done the right steps 
anythin else is an issue, 

open or close becoming < 0 before index == n return
balance > 0 on index == n or  < 0 not add

backtracking is to have remove and keep across the thing 

"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()
        open , close, balance = 0 , 0 , 0

        for element in s:
            if element == '(':
                balance += 1
            elif element == ')':
                balance -= 1

            if balance == -1:
                # we can remove a close bracket
                close += 1
                balance += 1

        # can remvoe the excess opens that could never be closed
        open += balance

        # print("open : " , open , " : " , " close : " , close)

        curr = []

        def helper(index, o, c, bal):
            
            if bal <= -1 or o < 0 or c < 0:
                return 

            if index == len(s):
                if o == 0 and c == 0 and bal == 0:
                    # correct candidate 
                    res.add("".join(curr))
                
                return


            if s[index] == '(':
                # remove
                helper(index + 1 , o - 1 , c , bal)
                # add
                curr.append(s[index])
                helper(index + 1 , o , c , bal + 1)
                curr.pop()

            elif s[index] == ')':
                # remove
                helper(index + 1 , o , c - 1 , bal)
                # add 
                curr.append(s[index])
                helper(index + 1 , o , c , bal - 1)
                curr.pop()
            else:
                curr.append(s[index])
                helper(index + 1 , o , c , bal)
                curr.pop()


        helper(0 , open, close, 0)

        return list(res)
        