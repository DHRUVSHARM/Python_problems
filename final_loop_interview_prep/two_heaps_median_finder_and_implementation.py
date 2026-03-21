"""
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
simple freq map + bucket logic 
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
0 - 100 map + separate buckets in front and behind (single bucket for each of them)
less than 0 | 0 - 100 | greater than 100




1 , 10 ,             000 , 10

max     min
left , right

always insert in the one that is on the left

check if condition violated and fix


"""


# theory of the 2 heaps pattern and implemnting median finder
import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap 
        self.right = [] # min heap

    def balance(self):
        # balance based on the frontier elements if they exist after comparision 
        # check if left max value <= min right 
        # else push to right , pull out new valid value and push back to the left heap 
        if self.left and self.right:
            l_frontier , r_frontier = -1 * self.left[0] , self.right[0]
            if l_frontier > r_frontier:
                l_element = heapq.heappop(self.left)
                heapq.heappush(self.right , -1 * l_element)
                r_element = heapq.heappop(self.right)
                heapq.heappush(self.left , -1 * r_element)
    
    def addNum(self, num: int) -> None:
        # we add the num to the left heap 
        heapq.heappush(self.left , -1 * num)
        # balance based on the frontier 
        self.balance()
        # balance based on height mismatch, left will always be greater in size than right in this solution 
        if len(self.left) > len(self.right) + 1:
            # greater than one diff
            l_frontier = heapq.heappop(self.left)
            heapq.heappush(self.right , -1 * l_frontier)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            # we know atleast 2 0 case handled 
            return (-1 * self.left[0] + self.right[0]) / 2
        else:
            # always we know that the odd median will be the left frontier in this approach
            return -1 * self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()