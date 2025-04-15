import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = { i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])


        res = 0
        visit = set()
        minHeap = [[0, 0]]

        while len(visit) < N:
            dist, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += dist
            visit.add(node)

            for nei in adjList[node]:
                if nei[1] not in visit:
                    heapq.heappush(minHeap, nei)
        return res





print(Solution().minCostConnectPoints(
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
))
