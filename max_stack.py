import heapq

class MaxStack:

    def __init__(self):
        # a minheap that will store the tuple (element (max) , index(max) )
        self.maxElement = []
        # simple stack that will hold the order, and will store (element , index)
        self.s = []
        # always increasing counter index that will help maintain the relative order 
        self.index = 0
        # keep a set that will keep track of the removed indices
        self.removed_indices = set() 
                

    def push(self, x: int) -> None:
        self.index += 1
        self.s.append((x , self.index))
        heapq.heappush(self.maxElement , (-1*x , -1*self.index)) 
        
    def pop(self) -> int:
        # O(LOGN)
        # we will maintain the stack so that atleast the top element can be popped correctly
        # first we will pop the top element
        popped_element, index = self.s.pop()
        self.removed_indices.add(index)

        # remove already removed till next top
        while self.s and (self.s[-1][1] in self.removed_indices):
            self.s.pop()

        return popped_element      # return the top

    def top(self) -> int:
        # edge case covered
        return self.s[-1][0]  

    def peekMax(self) -> int:
        # here we need to remove the elements that may have been removed due to removal from stack to 
        # peek the max
        max_element = None
        while self.maxElement:
            element, index = heapq.heappop(self.maxElement)
            if -1*index in self.removed_indices:
                # remove 
                pass
            else:
                # found max 
                max_element = element * -1
                # push back
                heapq.heappush(self.maxElement, (element, index))
                break

        return max_element

    def popMax(self) -> int:
        # here also we need to remvoe the elements that may have been removed to pop the max, 
        # and make sure that the normal stack pop op is also called to ensure the top element stays current
        top_max_element = self.peekMax() 
        # remove the max
        _ , index = heapq.heappop(self.maxElement)
        self.removed_indices.add(-1*index)
        
        # can do sanity check to check the top_max element and the element
        # remove the unwanted elements to keep the stack current
        while self.s and (self.s[-1][1] in self.removed_indices):
            self.s.pop()

        return top_max_element

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
