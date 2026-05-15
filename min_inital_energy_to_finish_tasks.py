from typing import List

# You are given an array tasks where tasks[i] = [actuali, minimumi]:
"""

we can sort by the diff (min - actual)
"""

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : (x[1] - x[0]) , reverse=True)
        result , curr_energy = 0 , 0

        for index, element in enumerate(tasks):
            # consume the element reduce energy 
            actual , min_req = element
            if curr_energy < min_req:
                result += (min_req - curr_energy)
                curr_energy = min_req
                
            
            # curr_energy >= min_req >= actual 
            # can guarantee curr_energy >= actual

            curr_energy -= actual

        return result