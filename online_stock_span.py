"""

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

 
1 1 1 2 1 4 6 

"""


class StockSpanner:

    def __init__(self):
        self.index = 0 # start from zero
        self.s = [ ( float("inf") , self.index ) ] 

    def next(self, price: int) -> int:
        # we will maintain the stack in monotonic decreasing order
        self.index += 1
        while self.s and self.s[-1][0] <= price:
            self.s.pop() 
        
        result = self.index - self.s[-1][1]
        self.s.append((price, self.index))
        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)