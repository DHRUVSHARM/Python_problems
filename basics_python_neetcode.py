import heapq
from collections import deque
import math


# class definition
class MyClass:
    # Constructor

    __slots__ = "nums", "size", "extra_attr"

    def __init__(self, nums):
        # constructor
        # Create member variables
        self.nums = nums
        self.size = len(nums)
        self.extra_attr = None

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


if __name__ == "__main__":
    # this is how you comment !!!
    # multiline conditionals

    # s = "T-50"
    # number = int(s[1:])
    # print(number)

    # ch = 'a'
    # print('0' <= ch <= '9')

    n, m = 100, 99
    if (n > 20 and m < 100) and m > 100:
        print("correct", end="")
    else:
        print("false", end="! ")

    # default at end reverts to newline if end is not specified
    print("now testing loops ")
    # loops with ranges , the end limit is never included
    for i in range(5, 0, -1):
        print(i)

    print("now talking about decimal division stuff !!")
    num, denom = -5, 2
    # result = num / denom
    # print(type(result))
    # simple / does decimal division
    print(num / denom)
    # print(result)

    # if we want to have integer division we use // but note that python rounds down for +ve and
    # -ve numbers unlike towards 0 like in the case of c++
    print(num // denom)
    # to counter this we can convert to int after using /
    print(int(num / denom))
    print("test extra !!!")
    print(int(-27 / 10))
    print("modulo")
    # negative modulo has weird behaviour unlike c++
    print(10 % 3)
    print(-10 % 3)
    # normal behaviour . using math functions op is float
    print(int(math.fmod(-10, 3)))
    print("math functions ..")
    print(math.pow(2, 3))
    print(math.sqrt(2))
    print(math.floor(num / denom))
    print(math.ceil(num / denom))

    print("infinite peak values ")
    # we need max or min values for comparison, note that integers are infinite in
    # python

    print(float("inf"))
    print(float("-inf"))

    print(-2.0 > float("inf"))

    print("\narrays")
    # arrays are in the form of lists
    arr = [1, 2, 3]
    # method to use array as a stack
    print(arr)
    arr.append(4)
    arr.append(5)
    print(arr)
    arr.pop()
    arr.pop()
    print(arr)

    arr.insert(1, 7)
    print(arr)

    arr[0] = 0
    arr[3] = 0
    print(arr)

    # Initialize arr of size n with default value of 1
    n = 5
    arr = [1] * n
    print(arr)
    print(len(arr))

    # Careful: -1 is not out of bounds, it's the last value
    arr = [1, 2, 3]
    print(arr[-1])

    # Indexing -2 is the second to last value, etc.
    print(arr[-2])

    # Sublist (aka slicing)
    arr = [1, 2, 3, 4]
    print(arr[1:3])

    # Similar to for-loop ranges, last index is non-inclusive
    print(arr[0:4])
    # But no out of bounds error
    print(arr[0:10])

    # Unpacking
    a, b, c = [1, 2, 3]
    print(a, b, c)

    # Be careful though, this throws an error
    # a, b = [1, 2, 3]

    # Looping through arrays
    nums = [1, 2, 3]

    # Using index
    for i in range(len(nums)):
        print(nums[i])
    # Without index
    for n in nums:
        print(n)
    # With index and value
    for i, n in enumerate(nums):
        print(i, n)
    # Loop through multiple arrays simultaneously with unpacking
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    for n1, n2 in zip(nums1, nums2):
        print(n1, n2)
    print("************ zip ***************")
    for obj in zip(nums1, nums2):
        print(obj, type(obj))
    print("************ zip ***************")

    # Reverse
    nums = [1, 2, 3]
    nums.reverse()
    print(nums)

    # Sorting
    arr = [5, 4, 7, 3, 8]
    arr.sort()
    print(arr)

    arr.sort(reverse=True)
    print(arr)

    arr = ["bob", "alice", "jane", "doe"]
    arr.sort()
    print(arr)

    # Custom sort (by length of string)
    arr.sort(key=lambda x: len(x))
    print(arr)

    # List comprehension
    arr = [i for i in range(5)]
    print(arr)

    # 2-D lists
    arr = [[0] * 4 for i in range(4)]
    print(arr)
    print(arr[0][0], arr[3][3])

    # This won't work as you expect it to
    # arr = [[0] * 4] * 4

    print("********************************************")
    arr = [[i for i in range(0, 5)] for _ in range(0, 5)]
    for row in arr:
        print(str(row))

    print("string stuff ")
    # Strings are similar to arrays, but are immutable
    s = "abc"
    print(s[0:2])

    # But they are immutable, this won't work
    # s[0] = "A"

    # This creates a new string
    s += "def"
    print(s)

    # Valid numeric strings can be converted
    print(int("123") + int("123"))

    # And numbers can be converted to strings
    print(str(123) + str(123))

    # In rare cases you may need the ASCII value of a char
    print(ord("a"))
    print(ord("b"))

    # Combine a list of strings (with an empty string delimiter)
    strings = ["ab", "cd", "ef"]
    print("_".join(strings))

    print("  **** deque *** ")
    # deque can be used for queue as well as a stack
    # inside deque we can keep iterables note that
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)

    print(queue)
    while len(queue):
        print("removing element : " + str(queue.popleft()))

    queue.appendleft(1)
    queue.appendleft(2)

    print(queue)

    print("information on sets")
    mySet = set()
    for i in range(0, 5):
        mySet.add(i)
    print(mySet)

    # or you can do set comprehension
    mySet = {i for i in range(0, 5)}
    print(mySet)

    print(100 in mySet)
    print(1 in mySet)

    mySet.remove(1)
    print(mySet)

    print("dictionary")
    # dictionary comprehension
    myDict = {i: 2 * i for i in range(0, 5)}
    print(myDict)
    myDict[100] = 1000
    for key, val in myDict.items():
        print(str(key) + " : " + str(val))
    myDict.pop(100)
    for key, val in myDict.items():
        print(str(key) + " : " + str(val))

    # tuples can be used as keys for dictionaries or entries in hashsets
    # but note that tuples are immutable
    checker = set()
    checker.add((1, 2))
    print(checker)

    print("heaps and priority queue stuff !!!")
    # we use heapq for pq and heap stuff
    # by default heapq is min-heap
    # under the hood array style
    minheap = []

    # push operations are logn
    heapq.heappush(minheap, 3)
    heapq.heappush(minheap, 2)
    heapq.heappush(minheap, 1)

    print("this is the heap under the hood : " + str(minheap))
    # notice that the under the hood list is not sorted exactly it's actually a list

    # popping all elements like this will have net complexity as nlogn
    while len(minheap):
        print("element out is as : " + str(heapq.heappop(minheap)))

    # now to implement a max heap we just make sure that the elements are made negative
    maxheap = []

    # push operations are logn
    heapq.heappush(maxheap, -3)
    heapq.heappush(maxheap, -2)
    heapq.heappush(maxheap, -1)

    print("this is the heap under the hood : " + str(maxheap))
    # notice that the under the hood list is not sorted exactly it's actually a list

    # popping all elements like this will have net complexity as nlogn
    while len(maxheap):
        print("element out is as : " + str(-1 * heapq.heappop(maxheap)))

    # finally we can create a heap in o(n) time using heapify
    # this will create an inplace heap hence we can do this in linear time
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    print("currently the heap is " + str(arr))

    while len(arr):
        print("the element out is : " + str(heapq.heappop(arr)))

    print("************************************************")
    print("very important function stuff !!!")

    # using non local allows variable x to be bound to the nearest outer scope
    # excluding global variables
    def outer():
        # first we enter here no access to x here
        # print(str(x)) error
        def inner():
            # in here no access to x
            # print(str(x)) error
            def innermost():
                # here note that the x here is having nonlocal, we have changed the nearest
                # outer x except global scope
                nonlocal x
                x = 3
                # inner x also changed

            # new x here
            x = 2
            innermost()
            # the above x is changed due to nonlocal
            if x == 3:
                print("Inner x has been modified")
            # now the changes will not propagate out from here

        # entry pt here
        x = 1
        inner()
        # no change
        if x == 3:
            print("Outer x has been modified")
        # not modified

    # declared here for the first time
    x = 0
    outer()
    if x == 3:
        print("Global x has been modified")

    print("\n another example !!")

    def outer(a, b):
        c = "c"

        def inner():
            # if you only want access for computation you don't need non local
            # nonlocal c
            # c = "m"
            # simple use can be done anyways
            return a + b + c

        result = inner()
        print("the modified c is : " + str(c))
        return result

    print(outer("a", "b"))

    print("******************************************************")
    print("last example stuff")

    def double(arr, val):
        def helper():
            # Modifying array works
            for i, n in enumerate(arr):
                arr[i] *= 2

            # will only modify val in the helper scope
            # val *= 2

            # this will modify val outside helper scope
            nonlocal val
            val *= 2

        helper()
        print(arr, val)

    nums = [1, 2]
    val = 3
    double(nums, val)

    print("\nall about classes in python required in our case")
    myObj = MyClass([1, 2, 3])
    print(myObj.getLength())
    print(myObj.getDoubleLength())
