"""
1) 0 <= val <= 109

2) At most 2 * 104 calls will be made to push and pop.

4) It is guaranteed that there will be 
at least one element in the stack before calling pop.
"""

# [5  ,7  ,5 , 7 , 4 , 5 ]
# maps element -> frequency
# frequency -> [elements relative order]
# 5 : 0 , 7:0 , 4:1
# 1 : [4]
# max freq : 1
# note that the max freq will move up or down in +1 / -1 increments / decrements
import collections

class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq_to_occ = collections.defaultdict(list)
        self.freq = collections.defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq += 1
        self.freq_to_occ[self.freq[val]].append(val)



    def pop(self) -> int:
        # here, the pop op will be called only when the stack is not empty
        removed_item = self.freq_to_occ[self.max_freq].pop()
        self.freq[removed_item] -= 1
        if not len(self.freq_to_occ[self.max_freq]):
            self.max_freq -= 1
        
        return removed_item



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()