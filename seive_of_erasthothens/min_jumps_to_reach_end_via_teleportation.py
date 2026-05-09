from typing import List
# modified seive + bfs approach 
# non prime step : can move adjacent i + 1  , i - 1
# seive
# you start at index 0 

# 15   :  5
# keep pulling out factors, smallest to largest, 
# base case is to visit at 1 

# precompute a seive
def helper(limit):
    # seive[i] : represent the first prime factor
    seive = [-1] * (limit)
    seive[1] = 1 
    seive[0] = 0 
    index = 2
    while index * index <= limit:
        # check if prime 
        if seive[index] == -1:
            for j in range(index*index , len(seive) , index):
                seive[j] = index  # store the smallest factor 
        
        index += 1
    
    return seive

# seive will give req info for all <= limit
# 1 <= nums[i] <= 106
limit = 10**6 + 5
seive = helper(limit) # computed once

import collections
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        # print(len(seive))
    
        distances = {0 : 0} # start at the zero index
        # bucket has to be enumerated 
        # bucket[element] = [indices that are divisible by element] element is composite 
        bucket = collections.defaultdict(list)

        for index, element in enumerate(nums):
            # composite number 60 , bucket[2] = [index] # will hit the prime element keys 
            factor = seive[element]
            while factor != -1 and factor != 1:
                bucket[factor].append(index)
                while element % factor == 0:
                    element = element // factor
                factor = seive[element]
            # at a prime number if 1 skip since 1 is not prime  
            if factor == -1:
                # last prime factor
                bucket[element].append(index)

        # print(bucket)
        
        # q will store (index, element)
        q = collections.deque([(0 , nums[0])])

        while len(q):
            index, element = q.popleft()

            # composite / prime, can move left or right only
            if index - 1 >= 0 and index - 1 not in distances:
                distances[index - 1] = distances[index] + 1
                q.append((index - 1, nums[index - 1]))
            if index + 1 < n and index + 1 not in distances:
                distances[index + 1] = distances[index] + 1
                q.append((index + 1, nums[index + 1]))

            if seive[element] == -1:
                # prime number can teleport  
                for new_index in bucket[element]:
                    if new_index not in distances:
                        # visited distances will handle the self loop case as well , the only prime we can
                        # therefore hit from here is the same element but with different index
                        distances[new_index] = distances[index] + 1 # teleport 
                        q.append((new_index , nums[new_index]))
                bucket[element].clear() # remove 


        return distances[n - 1]