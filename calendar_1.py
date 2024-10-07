class TreeNode:
    def __init__(self , start , end):
        self.left = None
        self.right = None
        self.val = (start , end)



class MyCalendar:

    def __init__(self):
        # create a root
        self.root = TreeNode(-1 , -1)


    def book(self, start: int, end: int) -> bool:
        
        def helper(node , start , end) -> bool:
            s , e = node.val
            if end <= s:
                if not node.left:
                    # create it 
                    node.left = TreeNode(start , end)
                    return True
                
                return helper(node.left , start , end)
            elif start >= e:
                if not node.right:
                    # create it 
                    node.right = TreeNode(start , end)
                    return True
                return helper(node.right , start , end)
            else:
                # overlap
                return False
    


        if self.root.val[0] == -1 and self.root.val[1] == -1:
            # the first node added will be directly on to the root
            self.root = TreeNode(start , end)
            return True
        
        else:
            # use the recursive helper to get a solution
            return helper(self.root , start , end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)