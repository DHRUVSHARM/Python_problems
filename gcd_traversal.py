import collections
from typing import List

"""
        def pf(n):
            prime_factors, f = [], 2

            while f * f <= n:
                if n % f == 0:
                    prime_factors.append(f)
                    while n % f == 0:
                        n = n // f

                f += 1
            if n > 1:
                prime_factors.append(n)
"""


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        f_to_index = collections.defaultdict(int)
        adj = {index : [] for index in range(len(nums))}

        for index, n in enumerate(nums):
            # find the prime factorization
            f = 2
            while f * f <= n:
                if n % f == 0:
                    # factor found
                    if f not in f_to_index:
                        # need to create node
                        f_to_index[f] = index
                    else:
                        # we need to attach this index
                        adj[index].append(f_to_index[f])
                        adj[f_to_index[f]].append(index)
                    while n % f == 0:
                        n = n // f

                f += 1
            if n > 1:
                # factor found
                if n not in f_to_index:
                    # need to create node
                    f_to_index[n] = index
                else:
                    # we need to attach this index
                    adj[index].append(f_to_index[n])
                    adj[f_to_index[n]].append(index)

        # print(adj)
        # print(f_to_index)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(0)

        return True if len(visited) == len(nums) else False
