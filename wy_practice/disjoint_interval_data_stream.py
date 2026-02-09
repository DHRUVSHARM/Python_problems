from typing import List

"""

1 , 2 , 33 , 40 , 49 ...

1

1 , 1

1 , 3

1 , 1  3 , 3

1 , 2, 3 ,  7

1,1  3,3    7,7   


--------------------------------
1 : 3 , 7:7   -> logn 
get : n (linear)

help reduce the size of the stream  (better space complexity)

periodic merge ?

container : ordered keys

add : logn + n
get intervals

"""
from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        # in our case we will do a rebalance while merging to only store the 
        # joined intervals which is better for the follow up
        self.stream = SortedDict()

    def addNum(self, value: int) -> None:
        # we will add the number to the sorted dict, as a point interval
        # 1 ,1  2 , 2 , 3 , 3        6,8 
        # logn overall 
        # print("value to add : " , value)

        # lookup will cause issue , simple lookup via iteration
        # this is linear 
    
        """
        value_found = False
        for k, v in self.stream.items():
            if k <= value <= v:
                value_found = True
                break 
        """
        value_found = False
        find_index = self.stream.bisect_left(value)
        if find_index < len(self.stream):
            s , e = self.stream.peekitem(find_index)
            if s <= value <= e:
                value_found = True
        
        if (find_index - 1) >= 0:
            # check behind
            s , e = self.stream.peekitem(find_index - 1)
            if s <= value <= e:
                value_found = True

        if not value_found:
            self.stream[value] = value
        else:
            # value is already in our maintained variables
            return

        # we are sure that the number key exists, can find it's index
        index = self.stream.index(value) # block maxima binary search + index lookup in the block 
        start , end = self.stream.peekitem(index) # iterators to find new interval
        old_start , old_end = start , end # old values to compare

        # find indices on either side
        lpos , rpos = index - 1 , index + 1
        # print(start , ":" , end)

        # logn 
        if lpos >= 0:
            # ps, pe is merged already 
            # ps , pe | s , e -> extend
            prev_s , prev_e = self.stream.peekitem(lpos)
            # print(prev_s , ":" , prev_e)
            if start - prev_e == 1:
                start = prev_s

        if rpos < len(self.stream):
            # s , e | ns , ne -> extend
            next_s , next_e = self.stream.peekitem(rpos)
            # print(next_s , ":" , next_e)
            if next_s - end == 1:
                end = next_s
            
        
        # we will compress the stream if changed 
        if start == old_start and end == old_end:
            pass
        else:
            endkey = self.stream[end]
            for element in range(start , end + 1):
                self.stream.pop(element , None)
            # endkey will be value of end
            self.stream[start] = endkey

        # print("stream state")
        print(self.stream)

    def getIntervals(self) -> List[List[int]]:
        # we compressed the intervals at insertion already
        # simple iteration in o(n)
        result = []
        for k , v in self.stream.items():
            result.append([k , v])
        return result

if __name__ == "__main__":
    # testing the SortedDict
    sd = SortedDict({1:"a", 2:"two", 3:"b", 10: "ten", 5:"c", 7:"d"})
    # inorder 
    for k, v in sd.items():
        print(k , " : " , v)
    
    # pop, insert in logn time 
    element = sd.pop(-1 , "default")
    print(element)
    sd[2] = "two" # logn 
    print(sd)

    # iterate over a range of keys effeciently , inclusive start and end  
    # this is like a binary search to find the start point then iterate 
    # so we say log(n) + range_size time complexity 
    for key in sd.irange(5 , 10):
        print(key , " : " ,  sd[key])

    # in case not present
    index = sd.bisect_left(-11)
    print(index)
    r_index = sd.bisect_right(-11)
    print(r_index)
    # in case key present
    index = sd.bisect_left(10)
    print(index)
    r_index = sd.bisect_right(10)
    print(r_index)

    # empty 
    newsd = SortedDict()
    index = newsd.bisect_left(11)
    print(index)
    # how to manage deletions and merges while iterating 
    # [keys ... ]
    # compression : [1 , 2 , 3] -> combine it 
    # n / k * (logn / k) - dense , if k increases  -> n / k
    # n - sparse