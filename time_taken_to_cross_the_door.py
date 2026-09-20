from typing import List

"""
n persons

labelled 0 to n - 1

array given is sorted, non decreasing : arrival 

arrival[i] = arrival time of the ith person at our door 

state[i] = {
    0 if enter
    1 if exit 
}


        0   1   2   3   4
arrival [0, 1,  1,  2,  4], 
state = [0, 1,  0,  0,  1]

arrival, index

time : 0 

exit :     |  (1 , 1)  (4, 4)   |
entry :    |  (0, 0)   (1 , 2)  (2 , 3)  |

"""

import collections
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        # state will be arrival_time, index

        ans = [-1 for _ in range(0 , n)]

        # exit is 1 entry is 1 
        # If multiple persons want to go in the same direction, the person with the smallest index goes first. , queue insertion will maintain this order
        exit, entry = collections.deque() , collections.deque()

        for index, element in enumerate(arrival):
            if state[index] == 1:
                exit.append((element, index))
            else:
                entry.append((element, index))

        curr_time = 0 # lowest possible time 
        prev_action = 1
        
        # print("exit : " , exit)
        # print("entry : " , entry)

        while len(entry) or len(exit):
            # print("\n")
            # print("exit : " , exit)
            # print("entry : " , entry)

            index = None # will be selected  

            if len(entry) and len(exit):
                # both are available 
                # we need to adjust the arrival times wrt to the arrival times
                # entry_arrival_time = max(curr_time, entry_arrival_time)
                if curr_time <  entry[0][0] and curr_time < exit[0][0]:
                    # we were waiting for atleast a second 
                    # reset to exit
                    prev_action = 1 # override for exit 

                entry_arrival_time, exit_arrival_time = max(curr_time , entry[0][0]) , max(curr_time , exit[0][0])
                # check if previous second was free overall


                if entry_arrival_time == exit_arrival_time:
                    # 2 are waiting 
                    # decision based on prevaction 
                    if prev_action == 1:
                        # do exit
                        _ , index = exit.popleft()
                        curr_time = exit_arrival_time
                    else:
                        # do entry 
                        _ , index = entry.popleft()
                        curr_time = entry_arrival_time
                else:
                    # pick earlier 
                    if entry_arrival_time < exit_arrival_time:
                        # entry first force entry 
                        prev_action = 0
                        _ , index = entry.popleft()
                        curr_time = entry_arrival_time
                    else:
                        # exit first force exit 
                        prev_action = 1
                        _ , index = exit.popleft()
                        curr_time = exit_arrival_time
                
            else:
                # only one is available 
                if len(entry):
                    # simple out 
                    arr , index = entry.popleft()
                    # use max 
                    curr_time = max(curr_time , arr) # in case they were waiting
                    
                else:
                    # simple out 
                    arr , index = exit.popleft()
                    # use max 
                    curr_time = max(curr_time , arr) # in case they were waiting 
            
            # print("the prev action : " , prev_action)
            # print("exit : " , exit)
            # print("entry : " , entry)
            ans[index] = curr_time # store for the current answer  
            curr_time += 1 # inc for the next

        return ans 