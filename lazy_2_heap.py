import collections
import heapq


class IntegerContainerImpl:

    def __init__(self):
        # TODO: implement
        self.freq = collections.defaultdict(int)
        self.size = 0
        # max
        self.left = []
        # min
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        # balance has to be maintained as a shared variable
        self.balance = 0

    # TODO: implement interface methods here
    def add(self, value: int) -> int:
        self.freq[value] += 1
        self.size += 1

        # remove the unwanted elements at the top
        # this does not affect the balance , took care of it while
        # marking for deletion (lazy deletion)
        median = self.get_median()

        if median is None:
            # first element which is being entered
            self.balance += 1
            heapq.heappush(self.left, -value)
            return self.size

        # we need to consider balancing and adding to the correct heap
        if value <= median:
            # add left
            self.balance += 1
            heapq.heappush(self.left, -value)
        else:
            # add right
            self.balance -= 1
            heapq.heappush(self.right, value)

        if self.balance > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
            self.balance -= 2
        elif self.balance < 0:
            heapq.heappush(self.left, -heapq.heappop(self.right))
            self.balance += 2

        print("balance ", self.balance)
        print(self.left, " , ", self.right)

        return self.size

    def delete(self, value: int) -> bool:
        print("delete : ", value)
        if value not in self.freq:
            return False

        # we need to find the location to delete from
        # note that we will not have the None return case here
        median = self.get_median()
        print("median , ", median)

        self.freq[value] -= 1
        self.size -= 1
        if self.freq[value] == 0:
            self.freq.pop(value)

        if value <= median:
            self.balance -= 1
        else:
            self.balance += 1

        if self.balance > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
            self.balance -= 2
        elif self.balance < 0:
            heapq.heappush(self.left, -heapq.heappop(self.right))
            self.balance += 2

        print("balance ", self.balance)
        print(self.left, " , ", self.right)

        return True

    def get_median(self) -> int | None:
        print("to get median ...")
        # print(self.left , " , " , self.right)
        if not self.left:
            return None

        while self.left and -self.left[0] not in self.freq:
            heapq.heappop(self.left)

        while self.right and self.right[0] not in self.freq:
            heapq.heappop(self.right)

        return -self.left[0] if self.left else None
