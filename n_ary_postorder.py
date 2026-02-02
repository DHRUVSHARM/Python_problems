from typing import List , Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:

    def postorder_without_stack(self, root: 'Node') -> List[int]:
        result = []

        def postorder(node):
            if node is None:
                return
            
            # visit all children before adding self
            for child in node.children:
                postorder(child)

            result.append(node.val)       

        postorder(root)
        return result

    def postorder(self, root: 'Node') -> List[int]:
        s , result = [root] , []

        while s:
            if s[-1] is None:
                node = None
                s.pop() # remove none 
                if s:
                    node = s.pop()
                if node is not None:
                    result.append(node.val)
            else:
                # push the children in reverse order , add a null in the beginning 
                # so that we can pop and add the val
                frontier = s[-1]
                s.append(None)
                for child in reversed(frontier.children):
                    s.append(child)

        return result