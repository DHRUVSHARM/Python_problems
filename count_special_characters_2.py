"""

hashmap

letter : [  -1 , -1 ]
            last occ    first occ of uppercase 
            this shows not seen 

            if both not -1 and uppercase - lowercase > 0
            count the letter 

"""

"""

hashmap

letter : [  -1 , -1 ]
            last occ    first occ of uppercase 
            this shows not seen 

            if both not -1 and uppercase - lowercase > 0
            count the letter 

"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        data = {}

        for index , letter in enumerate(word):
            
            ord_diff , is_lower = None , True

            if 0 <= ord(letter) - ord('a') <= 25:
                ord_diff = ord(letter) - ord('a')
            else:
                is_lower = False
                ord_diff = ord(letter) - ord('A')

            # check 
            if ord_diff not in data:
                data[ord_diff] = [-1 , -1]
            
            if is_lower:
                # lowercase 
                data[ord_diff][0] = index
            else:
                # uppercase 
                if data[ord_diff][1] == -1:
                    data[ord_diff][1] = index
        
        ans = 0
        for k , v in data.items():
            l_idx, u_idx = v
            if l_idx != -1 and u_idx != -1 and u_idx - l_idx > 0:
                ans += 1
        
        return ans