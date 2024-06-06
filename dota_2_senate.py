"""
2 big takeaways
str -> list(char's) conversion possible
deque can be used to maintain relative order
"""

from collections import deque

if __name__ == "__main__":
    str = "dhruv"
    arr = list(str)
    print(arr)

    for i, ele in enumerate(list(str)):
        print(i, ele)


# greedy approach with 2 deque used to efficiently track relative difference and
# track the circular movement of the 2 elements
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n, r_deque, d_deque = len(senate), deque(), deque()

        for index, element in enumerate(list(senate)):
            if element == "R":
                r_deque.append(index)
            elif element == "D":
                d_deque.append(index)

        while len(r_deque) != 0 and len(d_deque) != 0:
            r, d = r_deque.popleft(), d_deque.popleft()
            if r < d:
                r_deque.append(r + n)
            else:
                d_deque.append(d + n)

        return "Radiant" if len(r_deque) != 0 else "Dire"
