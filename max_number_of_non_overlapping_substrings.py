class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        """
        0   1   2   3   4   5   6   7      8   9   10
        a   d   e   f   a   d   d   a  |   c   c   c
                        i

        not seen means new interval 
        start = 0, end = 3 

        a : [0 8]
        d : [1 6]
        e : [2 2]
        f : [3 3]
        c : [8 10]

        we can get components by detecting overlap 

        0 ---------------- 7
           1------------6
               33

        # we need to understand that the solution becomes simple greedy if we can get all valid intervals 
        then we just need to pick up the correct ones

        each char will have one valid interval candidate which we need to test
        we test if whether this can be the start point

        NOT all can be the start point 
        if we consider one as the start point, then , we check 
            if some elmenent has < start abort 
            if element > end, extendm, keep checking since 1 can violate, 
            if withing then ok
            if can reach end without violating means found one, with that as start 
            do for all chars

            apply greedy to result 
            since we need the selections we can easily use the index maps to build the strings and return the answer 
            careful about being linear, so we only build final answer with join 
        """


        n = len(s)

        occ = {}

        for index, element in enumerate(s):
            if element not in occ:
                occ[element] = [index , index] # put start index and end index as same 
            else:
                occ[element].pop()
                occ[element].append(index) # append new end index 


        # we build for each key candidate 
        valid_intervals = []
        for element in occ.keys():
            is_valid = True
            start, end = occ[element]
            index = start

            # goal is to be able to reach the end 
            while index < end:
                if occ[s[index]][0] < start:
                    # some element has and occ previously so invalid
                    is_valid = False
                    break
                elif occ[s[index]][1] > end:
                    # this window needs to be extended to accomodate the current seen element
                    end = occ[s[index]][1]
                else:
                    # these can stay within this range <= <=
                    pass
                index += 1

            if is_valid:
                valid_intervals.append([start , end]) # inclusive [start , end]
        

        # now we have the valid intervals idea is to sort by end time 
        """
        0 --------------- 0
            0 ------------------0
                0--------------------------0
                                                0 --------0 
        
        """

        valid_intervals.sort(key=lambda element : (element[1] , element[0])) # in case of same end time, priortize the smaller length 
        ans , index = [] , 0

        # sentinel not needed we can use our answer to build the final  
        while index < len(valid_intervals):
            st , ed = valid_intervals[index]
            if len(ans) == 0:
                ans.append([st, ed])     
            else:
                if st > ans[-1][1]:
                    ans.append([st , ed])
            index += 1

        return [s[start : end + 1] for start, end in ans]