"""
max_freq , global freq 
freq map

map
freq : stack 


"""
class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq = {}
        self.occ = {} # map the freq to the stack         

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        
        # increment the freq
        self.freq[val] += 1

        if self.freq[val] not in self.occ:
            self.occ[self.freq[val]] = []
            self.max_freq += 1 # new greatest freq 

        self.occ[self.freq[val]].append(val)

    def pop(self) -> int:
        # atleast one element before calling pop
        # print(self.max_freq)
        # print(self.occ)
        frontier = self.occ[self.max_freq].pop()
        if len(self.occ[self.max_freq]) == 0:
            # this frequency no longer exists
            self.occ.pop(self.max_freq)
            self.max_freq -= 1
        
        self.freq[frontier] -= 1
        return frontier

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()