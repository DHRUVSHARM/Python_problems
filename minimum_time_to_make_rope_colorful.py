class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        left , maximal_time , needed_time , running_sum = 0 , float("-inf") , 0 , 0
        for r in range(0 , len(colors)):
            if colors[r] != colors[left]:
                # need to add up the previous continuous substr
                # need to be at least greater than 1 in size
                if (r -left) > 1:
                    needed_time += (running_sum - maximal_time)
                # reset for next 
                maximal_time = float("-inf")
                running_sum = 0
                left = r

            maximal_time = max(maximal_time , neededTime[r])
            running_sum += neededTime[r]

        # NOTE we used r in a for loop so it will be 4 outside     
        # do not use it like we would for a while loop
        # print("r  , left : " , r ,  " " , left)
        if (len(colors) - left) > 1:
            needed_time += (running_sum - maximal_time)
        
        return needed_time