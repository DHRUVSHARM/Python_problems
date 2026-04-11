from typing import List

"""

observations 

logs [ sid , time ]

Input: 

n = 3, 

logs = [[1,3],[2,6],[1,5]], 


sort by the time 

           lr
3 , 1      5 , 1       6 , 2
                       

                        

queries = [10,11]
5 , 10      6 , 11

qi            



while qi:


    for r in ramhe()
        while l < r and logs[l] < qi[0]:
            remove[l]
            l += 1
        
        # add to current set 

        set.add(logs[r])


1           2
n = 3 



Output: [1,2]
Explanation: 
For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.


"""
import collections
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sort by time the logs 
        log_arr = [(time , sid) for sid , time in logs]
        log_arr.sort()

        queries = [(time - x , time , index) for index , time in enumerate(queries)]
        queries.sort()

        result = collections.defaultdict()
        # map the query to the server set 

        query_index , left , right = 0 , 0 , 0  # -1 indicates non processed as of now 
        subans = {}
        server_count = 0

        while query_index < len(queries):

            while left < len(log_arr) and log_arr[left][0] < queries[query_index][0]:
                # skip
                if log_arr[left][1] in subans:
                    subans[log_arr[left][1]] -= 1
                    if subans[log_arr[left][1]] == 0:
                        server_count -= 1
                        subans.pop(log_arr[left][1])
                left += 1
            
            # print("left : " , left)
            # this is start of valid window , ff the right if not further ahead 
            if right < left:
                right = left
            
            while right < len(log_arr) and queries[query_index][0] <= log_arr[right][0] <= queries[query_index][1]:
                if log_arr[right][1] not in subans:
                    subans[log_arr[right][1]] = 0
                    server_count += 1

                subans[log_arr[right][1]] += 1
                right += 1

            # print("left : " , left , " " , "right : " , right)
            # print(subans)
            result[queries[query_index][2]] = n - server_count

            query_index += 1
        
        ans = []
        for index in range(0 , len(queries)):
            ans.append(result[index])

        return ans 