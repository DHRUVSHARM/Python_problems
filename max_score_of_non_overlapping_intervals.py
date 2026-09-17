from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        """
        here the tie breaking for optimal answer is extended by picking smaller lexicographically answer 

        dp[i][k] = max score of non overlapping (not sharing ends as well) from 0 ... i and at most k 
         - (
            max_score, [] in case of tie breaks we take the larger len , lex
         )

        intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

        1 ----- 3
        1 ------------- 5
                    4---5
                            6---7
                            6---------------9
                                        8---9


        dp[i][k] = max(
        
            dp[i - 1][k],
            consider rho = end < curr_start (bisect_left , start) - 1 
            dp[rho][k - 1]
        )        

        for comparing we compare score, if tie, lex
        dp[i][0] = [0 , []]
        for i in range(0 , n)
        
        for i in range(0 , n):
            for k in range(1 , 5):
                pass
        
        return dp[n - 1][4][1]

        """

        n = len(intervals)
        # older mappings need to be preserved 
        intervals = [[x[0] , x[1] , x[2] , index] for index , x in enumerate(intervals)]
        intervals.sort(key=lambda e : (e[1] , e[0] , e[3])) # if intervals are the same we can keep the earliest index first
        # bisectleft will pick first from left and pickup that 
        # sort by end times and on conflict 

        # seed with lexicographically largest answer for correctness guarantees
        dp = [[[float("-inf") , [float("inf")] * 5] for _ in range(4 + 1)] for _ in range(0 , n)] 

        for segment_limit in range(1 , 5):
            # we can only select the current one for index 0, list will always be the zero index  
            dp[0][segment_limit] = [intervals[0][2] , [intervals[0][3]]]
        
        # we need to seed for the k - 1 case and it can end on any index
        for i in range(0 , n):
            dp[i][0] = [0 , []]

        for index in range(1 , n):
            for segment_limit in range(1 , 5):
                # the prev can be taken as it is
                dp[index][segment_limit] = dp[index - 1][segment_limit] # seed with previous 

                # < >= , < curr_start
                idx = bisect_left(intervals , intervals[index][0] , 0 , index,  key=lambda element : element[1]) - 1
                curr_score, curr_ans = intervals[index][2] , [intervals[index][3]] # add current index 

                if idx == -1:
                    # previous stuff is empty 
                    pass
                else:
                    # we can use the previous one 
                    prev_score, prev_ans = dp[idx][segment_limit - 1]
                    curr_score += prev_score
                    curr_ans = prev_ans + curr_ans
                    # need to keept the indices collected sorted
                    curr_ans.sort()

                if curr_score > dp[index][segment_limit][0]:
                    # update
                    dp[index][segment_limit] = [curr_score , curr_ans]
                elif curr_score == dp[index][segment_limit][0]:
                    if curr_ans < dp[index][segment_limit][1]:
                        # use smaller
                        # print("curr_ans : " , curr_ans , " : " , "dp[index][seglimit][1] " , dp[index][segment_limit][1])
                        dp[index][segment_limit] = [curr_score , curr_ans]
                    else:
                        # keep previous, no update 
                        pass
                else:
                    # keep previous , no update  
                    pass
                    

        return dp[n - 1][4][1] # return selected list 