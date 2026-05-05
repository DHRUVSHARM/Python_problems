class Solution:
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

        a a c a
        a |a a c a| a a c
        """

        # can concatenate the goal and reversed and find s in this string 
        goal = goal + goal

        return s in goal 
