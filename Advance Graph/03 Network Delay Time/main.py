import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i+1:[] for i in range(n)}

        for src, dest, time in times:
            adj[src].append([dest, time])

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:

            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            t = time

            for nei, n_time in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (time+n_time, nei))
        return t if len(visit) == n else -1



print(Solution().networkDelayTime(
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]],
    n = 4,
    k = 1
))

# Output: 3

# Network Delay Time
# You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).
#
# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.
#
# Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.
#
# Example 1:
#
#
#
# Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
#
# Output: 3
# Example 2:
#
# Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
#
# Output: -1
# Constraints:
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 1000
