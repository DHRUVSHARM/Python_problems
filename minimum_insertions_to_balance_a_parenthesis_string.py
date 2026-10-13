class Solution:
    def minInsertions(self, s: str) -> int:
        """
        if we seed eacg open with 2 and try to balnce with 2 closing, 
        then the only time we go negative we add while allowing positive
        in the end we can just add the open ones
        
        one open needs 2 close 

        )
        open = 0 close = -1

        ))
        open = 0 close = -2

        (
        open = 1 , close = 0

        () .. (
        ) .. (
        )) .. (
        """
        ans = 0
        balance = 0
        prev = None

        for element in s:
            if element == '(':
                if balance < 0:
                    if abs(balance) % 2 == 1:
                        # add open and close on the other end 
                        ans += 2
                        balance += 1

                    ans += (abs(balance) // 2)
                    balance = 0
                
                # an even balance means we have open brackets that can always be 
                # closed at the end after exhausting all possibilities
                # but odd means there is one less closing and that needs to be remedied
                # reason is because that is a partial open bracket which cannot be closed
                # once the next open bracket comes around and has to be balanced now 
                elif balance > 0 and (balance % 2) == 1:
                    ans += 1
                    balance -= 1
                # now add after balancing 
                balance += 2
            else:
                # closing is still considered 1 
                balance -= 1
            prev = element

        # print("balance : " , balance)
        # balance may be positive or negative
        if balance < 0:
            if abs(balance) % 2 == 1:
                # add open and close on the other end 
                ans += 2
                balance += 1

            ans += (abs(balance) // 2)
            balance = 0
            
    
        # for every open 2 close 
        ans += balance
        return ans