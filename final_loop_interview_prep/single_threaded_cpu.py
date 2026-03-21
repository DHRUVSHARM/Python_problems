from typing import List

"""


task[i] = [enque time , processing time]
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]

eq time = 4
time = 3

2 , 4 , |  3,  2            

if eq_time >= time
time eq_time + process_tiem




time = 3



time = 3
Output: [0,2,3,1]


idle : idle 
greedy select shortest available task , heap(processing time, index ) (min heap ?)
cannot stop 

time process in inc oder of enque time 


time = 5
(1, 2)  ? pop, 

4 , 1



push to heap if empty 


time = 3
[ ]

lft = 5                                i
Input: tasks = [           |  [100,1]]



"""
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(t[0] , t[1] , index) for index , t in enumerate(tasks)]
        tasks.sort() # sort in increasing order of enqueue time 
        q = []
        last_finish_time , result , left = tasks[0][0] , [] , 0

        for r in range(0 , len(tasks)):
            eq_time, process_time , index = tasks[r]
      

            if last_finish_time >= eq_time:
                # idle, add to consider
                heapq.heappush(q , (process_time , index))
                # print("process_time : " , process_time)
                # print("task : " , tasks[r])
                # print("last finish time : " , last_finish_time)
                # print(q)
            else:
                while len(q):
                    t , i  = heapq.heappop(q) 
                    last_finish_time += t
                    result.append(i)
                    if last_finish_time >= eq_time:
                        break
                
                # at this point either empty , in which case means we can move last 
                if last_finish_time < eq_time:
                    last_finish_time = eq_time
                
                # now push to consider further
                heapq.heappush(q , (process_time , index))
            
        
        # remaining will be popped out in order and processed
        # print("q : " , q)
        while len(q):
            _ , i = heapq.heappop(q)
            # print(i)
            result.append(i)


        return result