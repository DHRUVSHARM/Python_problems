"""
constraints:
0 <= start < end <= 109
At most 1000 calls will be made to book.

here the range is too big to consider as fixed and 
the input is dynamic 
"""

class Event:
    def __init__(self , start , end , left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.start} , {self.end}"

class MyCalendar:

    def __init__(self):
        # will represent the node with range [0 , 10**(9))
        self.root = None
    
    def helper(self, node, startTime , endTime):
        if node is None:
            # we can insert here and return true indicating booked 
            return True , Event(startTime, endTime)
        
        
        # else we need to check overlap
        if endTime <= node.start:
            # can insert left
            res, lnode = self.helper(node.left, startTime , endTime)
            if res == True:
                node.left = lnode
                return res, node
            else:
                return res, None

        elif startTime >= node.end:
            # can insert right 
            res, rnode = self.helper(node.right, startTime , endTime)
            if res == True:
                node.right = rnode
                return res, node
            else:
                return res, None
            
        else:
            # overlap, and no overwrite 
            return False, None


    def book(self, startTime: int, endTime: int) -> bool:
        # can do using recursive helper 
        res, node = self.helper(self.root , startTime , endTime)
        if node is not None:
            self.root = node
        # print(self.root)
        return res


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)