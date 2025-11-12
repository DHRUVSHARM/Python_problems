from typing import List 
import collections

class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp , zero_one_count = collections.defaultdict(int) , collections.defaultdict(list)
        for index , element in enumerate(strs):
            zero_one_count[index] = [element.count('0') , element.count('1')]

        # memoization solution with early return 
        """
        def dfs(m , n , index):
            # print("index : " , index)
            if (m  , n ,  index) in dp:
                return dp[(m , n  , index)]
            
            # base cases 
            if index == len(strs):
                if m >= 0 and n >= 0:
                    return 0
                else:
                    return float("-inf")
                
            
            # dp case early return so that the memory does not blow up
            res = max(
                (1  + dfs(m - zero_one_count[index][0] , n - zero_one_count[index][1] , index + 1))
                  if (m - zero_one_count[index][0] >= 0 and n - zero_one_count[index][1] >= 0) else float("-inf"),
                dfs(m , n , index + 1)
            )

            dp[(m , n  , index)] = res
            return dp[(m , n  , index)]

        
        res = dfs(m , n , 0)
        return res if res >= 0 else 0
        """

        # dp solution
        for index in range(0 , len(strs)):
            zeroes , ones = zero_one_count[index][0] , zero_one_count[index][1]
            for m_count in range(m , zeroes - 1  , -1):
                for n_count in range(n , ones - 1 , -1):
                    # we stop here since there is no point looking if the number of zeroes / ones available is less than the requiremeent to 
                    # add the current str , exclude anyways skips 
                    dp[(m_count , n_count)] = max(1 + dp[(m_count - zeroes , n_count - ones)] , dp.get((m_count , n_count) , 0) )
        
        return dp[(m , n)]