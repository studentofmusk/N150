import heapq
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node: int) -> int:
        res = node
        while res != self.parent[node]:
            self.parent[res] = self.parent[self.parent[node]]
            res = self.parent[res]
        return res

    def union(self, node1, node2) -> int:
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return 0

        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return 1


class Solution:
    def MST(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        minHeap = []
        for n1, n2, weight in edges:
            heapq.heappush(minHeap, [weight, n1, n2])

        mst = []

        unionFind = UnionFind(n)

        while minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            mst.append([n1, n2])

        return mst

print(Solution().MST(
    n=5,
    edges=[
        [0, 1, 3],
        [1, 2, 2],
        [0, 2, 1],
        [2, 3, 4],
        [1, 4, 2],
        [4, 3, 1]
    ]
))


