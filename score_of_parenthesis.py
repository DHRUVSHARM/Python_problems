class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # we cam store a sentinel value representing the vps finished 
        # or no need just have to be zero 
        # if open bracket multiply current score while closing 
        # put the previous one add and pop i guess or maybe just add to a accumalator 
        """
            2
        (   (     ))
    


        (   (   )   | ( (   ) )   )         
        """
        
        acc = 0 
        st = []

        for element in s:
            if element == '(':
                st.append([element , 0])
            else:
                # close bracket is interesting 
                # we know vps in this case 
                if len(st):
                    _ , score = st.pop()
                    if len(st) == 0:
                        # means we can add this vps since it is complete and wont be part of any nesting 
                        acc += (1 if score == 0 else score)
                    else:

                        st[-1][1] += (2 * (1 if score == 0 else score)) # means nesting 
                else:
                    # we will never reach here 
                    pass

        return acc