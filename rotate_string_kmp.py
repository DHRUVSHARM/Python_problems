class Solution:

    def kmp(self, s, pattern):
        # linear alogrithm to find pattern in s 
        # return true if we can find else false

        # compute lps longest prefix that is also a suffix 
        """     len = 1
                a a c a 
        lps     0 i 2
        """
        lps = [0 for _ in range(0 , len(pattern))]
        length = 0 # current size of lps , represents the next index to consider for match
        # basically max length of prefix we have built up unitl this point  

        for index in range(1 , len(lps)):
            # mismatch go back to previous matched lps 
            while length > 0 and pattern[index] != pattern[length]:
                # move back 
                length = lps[length - 1]
            
            if pattern[index] == pattern[length]:
                length += 1
            
            lps[index] = length 

        """
                  i
        s   = a a x c a a a c
              
        p   = a a c a
        lps = 0 1 0 1
        """

        m , n = len(s) , len(pattern)
        i , j = 0 , 0

        while i < m and j < n:
            if s[i] == pattern[j]:
                i += 1
                j += 1
            else:
                # retract
                if j == 0:
                    # need to reset , new start point req 
                    i += 1
                else:
                    # can move back, go back at this point we had matched a part, most recent was a suffix
                    # we can at the least in the pattern go back and point at the next of the prefix  
                    j = lps[j - 1]
        
        return j == n


    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        """
        Input: s = "abcde", goal = "cdeab"
        Output: true
                    i
        a   a   c   b   
        a   a   c   x
        j

            1
        0      
        a   a   c   a

        a a c a
        a |a a c a| a a c
        """

        # can concatenate the goal and reversed and find s in this string 
        goal = goal + goal
        
        # we can find s in goal using the kmp algortihm 
        # return s in goal 
        return self.kmp(goal , s)
