# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

if __name__ == "__main__":
    a = []

    def foo():
        a.append(2)

    foo()
    print(a)


class Solution:
    final_result = []

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # the concept is that we need to move from the root
        s = collections.deque()

        def testing(curr):
            final_result = self.final_result
            print("curr : ", curr)
            print("final result : ", final_result)

            if len(final_result) == 0:
                return curr
                # we need to test the curr
            left, right = 0, 0
            while left < len(curr) and right < len(final_result):
                if curr[left] < final_result[right]:
                    return curr
                elif curr[left] > final_result[right]:
                    return final_result
                else:
                    # equal
                    left += 1
                    right += 1

            if len(curr) <= len(final_result):
                return curr
            else:
                return final_result

        def helper(node):
            if not node.left and not node.right:
                # this is a base leaf
                s.appendleft(node.val)
                # test for final ans
                self.final_result = testing(list(s))
                # final_result = ans
                # print("final result : " , final_result)
                s.popleft()
                return

            s.appendleft(node.val)
            if node.left:
                helper(node.left)

            if node.right:
                helper(node.right)
            s.popleft()

        helper(root)
        print(self.final_result)
        self.final_result = [chr(ord("a") + element) for element in self.final_result]
        return "".join(self.final_result)
