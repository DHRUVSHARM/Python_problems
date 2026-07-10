# Problem summary:
# - Infer a valid character order from words that are sorted according to an
#   alien alphabet. Return an empty string if the ordering is invalid.
#
# Approach:
# - Compare each adjacent pair of words and use the first differing character
#   to create a directed ordering edge.
# - Add all seen characters to the graph, and reject the invalid prefix case
#   where a longer word appears before its own prefix.
# - Run DFS to detect cycles in the character dependency graph.
# - Build indegrees and run Kahn's topological sort with a min heap to produce
#   a deterministic valid order.
#
# Pattern:
# - Topological sort on a directed graph, with DFS cycle detection and
#   heap-based Kahn's algorithm.
#
# Complexity:
# - Time: O(C + U log U + E log U), where C is total characters, U is unique
#   characters, and E is ordering edges.
# - Space: O(U + E).
#
# Example dry run:
# - Input: words = ["wrt", "wrf", "er", "ett", "rftt"].
# - Compare "wrt" and "wrf": first difference is t vs f, so add edge t -> f.
# - Compare "wrf" and "er": first difference is w vs e, so add edge w -> e.
# - Compare "er" and "ett": first difference is r vs t, so add edge r -> t.
# - Compare "ett" and "rftt": first difference is e vs r, so add edge e -> r.
# - Indegrees make w the first zero-indegree character; heap pops w, then e,
#   then r, then t, then f as edges are relaxed.
# - Output: "wertf".

import collections
import heapq
from typing import List

if __name__ == "__main__":
    # print('a' < 'A')
    print("a" < "z")
    print("z" < "a")
    print("a" == "a")

    h = ["z", "a"]
    heapq.heapify(h)

    while h:
        print(heapq.heappop(h))


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        if len(words) == 0:
            return ""
        # we will store the words here
        res = []
        adj = collections.defaultdict()

        for i in range(1, len(words)):
            j, k = 0, 0
            while j < len(words[i - 1]) and k < len(words[i]):
                if words[i - 1][j] not in adj:
                    adj[words[i - 1][j]] = set()
                if words[i][k] not in adj:
                    adj[words[i][k]] = set()

                if words[i - 1][j] == words[i][k]:
                    j += 1
                    k += 1
                elif words[i - 1][j] != words[i][k]:
                    # we need to create an edge
                    adj[words[i - 1][j]].add(words[i][k])
                    break

            if j < len(words[i - 1]) and k < len(words[i]):
                # break in bw
                while j < len(words[i - 1]):
                    if words[i - 1][j] not in adj:
                        adj[words[i - 1][j]] = set()
                    j += 1

                while k < len(words[i]):
                    if words[i][k] not in adj:
                        adj[words[i][k]] = set()
                    k += 1

            elif j == len(words[i - 1]) and k < len(words[i]):
                # prefix occurs earlier than the actual word , ok
                while k < len(words[i]):
                    if words[i][k] not in adj:
                        adj[words[i][k]] = set()
                    k += 1
            else:
                # prefix after the word , invalid
                return ""

        # print(adj)
        visited = collections.defaultdict(bool)

        # visited -> true if the node is visited and is in the current path , false if visited
        # not in the current path

        def dfs(node):
            if node in visited:
                return visited[node]

            # we are seeing this node for the first time
            # add to path
            visited[node] = True

            for neighbour in adj[node]:
                if dfs(neighbour):
                    # there was a loop here
                    return True

            visited[node] = False
            res.append(node)
            return visited[node]

        # now we need to do dfs and get the final answer
        # in lint code , this dfs is useful only for cycle detection
        for start in sorted(adj.keys()):
            # call dfs
            if dfs(start):
                # means a cycle was found
                return ""

        # we need to do the incoming one for the correct order output

        incoming = {n: 0 for n in adj.keys()}
        for src in adj:
            for dest in adj[src]:
                incoming[dest] += 1
        # print(incoming)
        # if there is a cycle then there will come a point where we will not be able to find the
        # starter element
        s, minHeap = [], []
        for key in adj.keys():
            if incoming[key] == 0:
                heapq.heappush(minHeap, key)

        while len(minHeap):
            element = heapq.heappop(minHeap)
            s.append(element)
            for neig in adj[element]:
                incoming[neig] -= 1
                if incoming[neig] == 0:
                    heapq.heappush(minHeap, neig)

        return "".join(s) if len(s) == len(adj.keys()) else ""
