import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': # type: ignore
        # size of schedule is atleast one 
        schedules = []
        for emp in range(0 , len(schedule)):
            for interval in range(0 , len(schedule[emp])):
                schedules.append((schedule[emp][interval].start , schedule[emp][interval].end ))
        # sort by the start time 
        schedules.sort()
        latest_free_time , result = [(-schedules[0][1] , schedules[0][0])] , [] # start with first employee
        # maxheap 

        for index in range(1 , len(schedules)):
            s , e = schedules[index]
            if s - (-1* latest_free_time[0][0]) >= 1:
                # can add an interval since we want times when all employees are free
                result.append((-1* latest_free_time[0][0] , s))
            # push to heap 
            heapq.heappush(latest_free_time , (-1 * e , s))

        return [Interval(s , e) for s , e in result] # type: ignore
    