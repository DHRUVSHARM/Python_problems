from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # we are given a DAG
        # storing
        incoming_vertices = {i: [] for i in range(0, n)}
        for u, v in edges:
            incoming_vertices[v].append(u)

        # these will be vertices with no incoming edges
        vertices = []
        for key, value in incoming_vertices.items():
            if len(value) == 0:
                vertices.append(key)

        return vertices
