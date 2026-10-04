class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        vps iff
        1) ""
        2) AB concatenation of 2 VPS
        3) (A) where A is a VPS 

        (   )   (   (   )   )   (   )
        1   1   1   2   

        1 , 2 , 1

        already a vps sequence 
        so at the very minimal we can spilt into empty and vps and get a valid answer
        otherwise we try to make it equal basically

        -------------------------------------------------------------------------------------------------------
        simple algo 
        keep track of the nesting depth 
        pick one with minimal
        complete vps scan
        keep moving 

        this way we can make mostly equal 

        final answer will be minimized as max(a , b) is the function 

        A                                   B
        ()                                 (())

        also the depth can simply be the lenght of the stack, if it represents the open brackets
        """

        ans = [0 for _ in range(0 , len(seq))]
        # 0 is a, 1 is b 

        zeroes , ones = 0 , 0

        st = []

        for index, element in enumerate(seq):
            if len(st) == 0:
                # we need to select the least one
                if zeroes <= ones:
                    curr = 0
                else:
                    curr = 1
            else:
                curr = curr ^ 1 # greedy

            if element == '(':
                st.append((element , index))
            else:
                element, idx = st.pop()
                ans[idx] = curr
                ans[index] = curr

        return ans

            
        