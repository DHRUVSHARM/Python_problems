# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return True

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return -1

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return []


import collections

if __name__ == "__main__":
    x = collections.deque([1, 2, 3])
    print(x)


class NestedIterator:
    __slots__ = "original_list", "flattened_list", "d"

    def dfs(self, curr):
        """
        populate the flattened list
        :return: None
        """
        for element in curr:
            if element.isInteger():
                self.flattened_list.append(element.getInteger())
            else:
                # we have a list
                self.dfs(element.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.original_list = nestedList
        self.flattened_list = []
        self.dfs(self.original_list)
        self.d = collections.deque(self.flattened_list)

    def next(self) -> int:
        if self.hasNext():
            front = self.d.popleft()
            return front
        else:
            return -1

    def hasNext(self) -> bool:
        return len(self.d) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
