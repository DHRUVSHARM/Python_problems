# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []

        def helper(node):
            if not node:
                return 
            
            if node.children:
                for child in node.children:
                    helper(child)
            
            ans.append(node.val)

        
        helper(root)

        return ans
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# iterative solution
class Solution:
    def postorder(self, root: "Node") -> List[int]:

        ans = []

        if not root:
            return ans

        nodes, visited = [root], [False]

        while nodes:

            # print([node.val for node in nodes] , " , " , [value for value in visited])

            if visited[-1] == False:
                node = nodes.pop()
                visited.pop()

                nodes.append(node)
                visited.append(True)

                if node.children:
                    for child in reversed(node.children):
                        nodes.append(child)
                        visited.append(False)

            else:

                ans.append(nodes.pop().val)
                visited.pop()

        return ans
