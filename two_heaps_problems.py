# we will solve problems based on the two heaps pattern
import heapq
from lazy_delete_heap import *
import itertools
from typing import List

if __name__ == '__main__':
    minHeap = [10, 9, 8]
    heapq.heapify(minHeap)
    print(minHeap)

    a = [1, 2, 3]
    b = ['x', 'y', 'z']

    for v, i in enumerate(zip(a, b)):
        print(v, " ", i)

# finding median
"""
class MedianFinder:
    # small is a max-heap and large is a min-heap
    __slots__ = "small", "large"

    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        # we add numbers always to the smaller heap
        heapq.heappush(self.small, -1 * num)

        # first we need to make sure of the less than invariant
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            top_element = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, top_element)
        # transfer always from large to small

        if len(self.small) > len(self.large) + 1:
            top_element = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, top_element)
        elif len(self.large) > len(self.small) + 1:
            top_element = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * top_element)

    def findMedian(self) -> float:
        # print(self.small , self.large)
        if abs(len(self.large) - len(self.small)) == 1:
            # odd sized array, we know size would be atleast 1
            if len(self.large) > len(self.small):
                return self.large[0]
            else:
                return -1 * self.small[0]
        else:
            # even sized array , we know size would be atleast 2
            return (self.large[0] + -1 * self.small[0]) / 2
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# problem 2
# we will use the previous problem along with the lazy delete operation

"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # we will need to keep to heaps which can support the delete operation
        small = lazy_heap()  # maxHeap
        large = lazy_heap()  # minHeap

        def addNum(index) -> None:

            small.add_task(index, -1 * nums[index])
            # task always added to small

            if small.get_size() and large.get_size() and (nums[small.peek()]) > nums[large.peek()]:
                t_index = small.pop_task()
                # print("top index : " , t_index)
                large.add_task(t_index, nums[t_index])

            if small.get_size() > large.get_size() + 1:
                # pop small move to large
                t_index = small.pop_task()
                # print("top index : " , t_index)
                large.add_task(t_index, nums[t_index])

            elif large.get_size() > small.get_size() + 1:
                # pop large move to small
                t_index = large.pop_task()
                # print("top index : " , t_index)
                small.add_task(t_index, -1 * nums[t_index])

        def findMedian() -> float:
            # print(small.get_size() , "**" , large.get_size())
            # print(small.pq , " ** " , large.pq)

            if abs(small.get_size() - large.get_size()) == 1:
                # odd sized array, we know size would be atleast 1
                if large.get_size() > small.get_size():
                    return nums[large.peek()]
                else:
                    return nums[small.peek()]
            else:
                # even sized array , we know size would be atleast 2
                return (nums[large.peek()] + nums[small.peek()]) / 2

        result, start, end = [], 0, 0
        while end - start + 1 <= k:
            addNum(end)
            # print(small.get_size() , "**" , large.get_size())
            # print(small.pq , " ** " , large.pq)
            end += 1
        result.append(findMedian())
        small.remove_task(start)
        large.remove_task(start)
        start += 1
        # print(start , end)

        while end < len(nums):
            addNum(end)
            end += 1
            result.append(findMedian())
            small.remove_task(start)
            large.remove_task(start)
            start += 1
            # print(start , end)

        return result
"""


# problem 3 IPO
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # we will need to use 2 heaps to solve this problem
        # w is the initial capital that we have

        # maxHeap based on profit that will store elements where the capital required is <= w
        # concept is to pop this and add it to the maximal capital
        # also note that we can use atmost k elements at max (imp)
        maxHeap = []

        # we will also need a minHeap to store the unreachable elements which will be inaccessible
        # until the element is popped. minHeap is based on minimal capital as then we can pop as many
        # into the maxHeap and use it for the next iteration to pop and continue the algo
        minHeap = []

        # this is going to be a greedy algo with 2 heaps where we will try make the
        # best local decision at every step

        # initialization condition , k is atleast one
        for index, value in enumerate(zip(profits, capital)):
            p, c = value
            if c <= w:
                heapq.heappush(maxHeap, (-1 * p))
            else:
                # here we have to keep track of the index as well to access the p value later on
                heapq.heappush(minHeap, (c, index))

        while k:
            if len(maxHeap):
                element = -1 * heapq.heappop(maxHeap)
                # print("element is : ", element)
                w += element
                # print("w is : ", w)
                while len(minHeap) and minHeap[0][0] <= w:
                    heapq.heappush(maxHeap, -1 * profits[heapq.heappop(minHeap)[1]])
            else:
                break

            # print(maxHeap, minHeap)
            k -= 1

        return w
"""