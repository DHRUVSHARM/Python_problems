"""
Docstring for waymo.find_median_from_data_stream

The median is the middle value in an ordered integer list. 

If the size of the list is even, there is no middle value, 

and the median is the mean of the two middle values.

There will be at least one element in the data structure before calling findMedian.

# incremental we can start with 2 heaps ?


# left  right
# push to left
# if left - right >= 1
# push to right
# 



1 , 2 3   4 , 5 , 6

"""


"""
TODO : NEED to understand and do the follow up
for restricted range 

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""


import heapq
class MedianFinder:

    def __init__(self):
        # heaps will be maintained as len(left) - len(right) <= 1 always
        self.left = [] # max heap
        heapq.heapify(self.left) 
        self.right = [] # min heap
        heapq.heapify(self.right)

                

    def addNum(self, num: int) -> None:
        # first we need to decide where to put the element
        left_frontier = -self.left[0] if len(self.left) else float("-inf") # heap property
        right_frontier = self.right[0] if len(self.right) else float("inf")
        # [-inf , +inf] initally 
        # [....left_f , right_f...] otherwise 

        if left_frontier <= num <= right_frontier:
            heapq.heappush(self.left , -num)
        elif num < left_frontier:
            heapq.heappush(self.left , -num)
        else:
            heapq.heappush(self.right , num)

        # [..num, left_f , rightf ... ]
        if len(self.left) - len(self.right) > 1:
            # move to right
            element = heapq.heappop(self.left)
            heapq.heappush(self.right , -element)
        elif len(self.right) - len(self.left) >= 1:
            # [..left_f , rightf .num... ]
            element = heapq.heappop(self.right)
            heapq.heappush(self.left , -element)
        else:
            # balanced 
            pass

        # print("adding num .. " , num)
        # print(self.left)
        # print(self.right)
        # print("\n")

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            # even , will be called at 2 
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()