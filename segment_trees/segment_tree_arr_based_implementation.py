from typing import List

"""
segment tree implementation
implementation will be like heap based array with gaps addressed without sentinel values
will return the sum of all elements in the range

# left child will always be even
# right child will be an odd index due to heap property

"""

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.tree = [0 for _ in range(0 , 2*self.size)]

        # set the leaf nodes
        for index in range(0 , len(nums)):
            self.tree[index + self.size] = nums[index]

        # move up the tree and set the node values
        # in this impl the 0 index node in the tree will not be used  
        for index in range(len(nums) - 1 , 0 , -1):
            self.tree[index] = self.tree[2*index] + self.tree[2*index + 1]
    
    def update(self, index: int, val: int) -> None:
        # for update we propagate index update at that point and then up the tree 
        # we assume index and val is valid input 
        tree_index = index + self.size
        self.tree[tree_index] = val
        while tree_index // 2 > 0:
            # propagate
            tree_index = tree_index // 2
            self.tree[tree_index] = self.tree[2*tree_index] + self.tree[2*tree_index + 1]
    
    def query(self, L: int, R: int) -> int:
        # sum query for [L , R] and we assume range is valid input 
        # compute for on the tree, the leaf nodes 
        l , r = self.size + L , self.size + R
        res = 0
        while l <= r:
            # first we check if the current left child is actually a left child 
            if l % 2 == 0:
                pass
            else:
                res += self.tree[l]
                l += 1
            
            if r % 2 == 1:
                pass
            else:
                res += self.tree[r]
                r -= 1
            
            l = l // 2
            r = r // 2
        
        return res