import collections
from typing import List

if __name__ == '__main__':
    arr = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    arr.sort()
    print(arr)

    collections.defaultdict(list)
    d = {1: [2]}

    # print(d[0])

    l = [1, 2, 3, 4, 5]
    print(l[:: -1])


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj, itinerary = collections.defaultdict(list), []
        for src, dest in tickets:
            adj[src].append(dest)

        def get_itinerary(current_stop):
            while adj[current_stop]:
                new_stop = adj[current_stop].pop()
                # lexicographically smallest is popped
                get_itinerary(new_stop)
            itinerary.append(current_stop)

        get_itinerary("JFK")
        return itinerary[::-1]
