class Solution:
    def smallestNumber(self, n: int) -> int:
        # we know that n is atleast 1
        mask = 1

        for bit in range(0 , 10):

            if n | mask == mask:
                break
            mask = (mask << 1) | 1
        
        return mask 

