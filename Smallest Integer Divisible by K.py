class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        start , states , steps , ans = 1 , set() , k  , 1

        # we should get a result in at max k - 1 steps
        while steps:
            
            rem = start % k
            
            if rem in states:
                return -1
            
            if not rem:
                break
            
            states.add(rem)

            start = ( (10 * start) + 1) % k
            steps -= 1
            ans += 1
        

        return ans
    