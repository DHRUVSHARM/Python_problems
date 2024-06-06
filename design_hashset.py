if __name__ == "__main__":
    pass


class ListNode:
    __slots__ = "value", "next"

    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next


# hashset implementation with chaining for collision handling
# limit is 10^6
class MyHashSet:
    __slots__ = "table", "size"

    def __init__(self):
        self.table = [ListNode(-1) for _ in range(10**4)]
        self.size = 10**4

    def add(self, key: int) -> None:
        prev = self.table[key % self.size]
        curr = prev.next

        while curr:
            if curr.value == key:
                return
            curr = curr.next
            prev = prev.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        prev = self.table[key % self.size]
        curr = prev.next

        while curr:
            if curr.value == key:
                prev.next = curr.next
                curr.next = None
                return
            curr = curr.next
            prev = prev.next

    def contains(self, key: int) -> bool:
        index = key % self.size
        curr = self.table[index]

        while curr:
            if curr.value == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
